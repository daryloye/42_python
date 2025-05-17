def NULL_not_found(object: any) -> int:
	match object:
		case int():
			print("Nothing:", object, type(object))
		case _:
			return 1
	return 0