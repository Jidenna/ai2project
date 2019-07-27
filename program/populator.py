import recognizer as rec
import image_generator as ig


def start():
    params = ["first name", "middle name", "last name",
              "birthdate", "civil status", "citizenship", "street name where you live", 
              "barangay where you live", "municipality or city where you live",
              "province where you live", "precinct number"]
    params = ["first name", "last name"]
    values = rec.populate(params)
#    ig.create_id(values)

    return values


if __name__ == "__main__":
    start()

