
def NULL_not_found(object: any) -> int:
	match object:
		case None:
			print("Nothing:", object, type(object))
		case object if str(object) == "nan":
			print("Cheese:", object, type(object))
		case object if str(object) == "0":	
			print("Zero:", object, type(object))
		case '':
			print("Empty:", object, type(object))
		case False:
			print("Fake:", object, type(object))
		case _:
			print("Type not Found")
			return 1
	return 0