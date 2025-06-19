http_error = 404
match http_error:
    case 200 | 201:
        print("Success!")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")