import grpc
from concurrent import futures

from protos import booking_pb2
from protos import booking_pb2_grpc
from protos import showtime_pb2
from protos import movie_pb2
from protos import user_pb2

import json

def createScheduleItem(date,movies)->showtime_pb2.Schedule:
    item:showtime_pb2.Schedule = showtime_pb2.Schedule(
        date=showtime_pb2.Date(date=date)
        )
    movies = map(lambda movie: movie_pb2.MovieID(id=movie),movies)
    item.movies.extend(movies)
    return item

def createBookingItem(booking):
    dates = list(map(
                    lambda date:
                        createScheduleItem(date=date["date"],movies=date["movies"]),
                    booking["dates"]
                ))
    booking_data = booking_pb2.BookingData(userId=user_pb2.UserID(id=booking['userid']))
    booking_data.date.extend(dates)
    return booking_data



class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('{}/data/bookings.json'.format("."), "r") as jsf:
            self.db:list[str] = json.load(jsf)["bookings"]

    def GetBookingByUserId(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.id:
                print("Booking found!")
                return createBookingItem(booking)

    def GetAllBookings(self, request, context):
        for booking in self.db:
            yield createBookingItem(booking)
 
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
