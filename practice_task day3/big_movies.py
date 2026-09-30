movies = []

for i in range(1, 3001):

    movies.append(
        f"""
        <tr>
            <td>Movie {i}</td>
            <td>₹{100 + (i % 200)}</td>
            <td>Screen {(i % 10) + 1}</td>
            <td>Available</td>
        </tr>
        """
    )


html = f"""
<!DOCTYPE html>
<html>

<head>
    <title>Large Movie Database</title>
</head>

<body>

<h1>Movie Database</h1>

<table>

<tr>
    <th>Movie</th>
    <th>Price</th>
    <th>Screen</th>
    <th>Status</th>
</tr>

{''.join(movies)}

</table>

</body>

</html>
"""


with open("big_movies.html", "w", encoding="utf-8") as file:

    file.write(html)


print("big_movies.html created successfully.")
print("Characters:", len(html))