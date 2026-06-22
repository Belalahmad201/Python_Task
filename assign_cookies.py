def find_content_children(greed, cookies):
    greed.sort()
    cookies.sort()

    child = 0
    cookie = 0

    while child < len(greed) and cookie < len(cookies):
        if cookies[cookie] >= greed[child]:
            child += 1
        cookie += 1

    return child


# Example Input
greed = [1, 2, 3]
cookies = [1, 1]

print("Maximum satisfied children:", find_content_children(greed, cookies))