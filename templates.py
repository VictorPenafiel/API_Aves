from string import Template

html_template = Template('''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
</head>
<body>

<h1>Aves de Chile</h1>
$body


</body>
</html>
''')

elem_template = Template('''

<h2>$titulo_es</h2>
<h3>$title_en</h3>
<img src='$url'>
''')
