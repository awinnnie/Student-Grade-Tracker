html_template = '''<!DOCTYPE html>
<html>
<head>
<style>
#customers {
  border-collapse: collapse;
  width: 100%;
}
* {
    font-family: 'Roboto', sans-serif;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
.id {
    cursor: pointer;
    color: blue;
    text-decoration: underline;
}
</style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
</head>
<body>

<h1>Students Report</h1>

<table id="customers">
  <tr>
    <th>Student ID</th>
    <th>Name</th>
    <th>Gender</th>
    <th>Date of Birth</th>
    <th>Section</th>
    <th>Science</th>
    <th>English</th>
    <th>History</th>
    <th>Maths</th>
    <th>Overall</th>
  </tr>
  $$REPLACE_ME$$
</table>
<script>
  const tds = document.querySelectorAll('.id');
  tds.forEach(td => {
    td.addEventListener('click', e => {
      const childNodes = e.target.parentNode.childNodes;
      const data = [];
      childNodes.forEach(node => {
        data.push(node.textContent);
      });
      document.body.innerHTML = `
        <h3>Student ID: ${data[0]}</h3>
        <h3>Name: ${data[1]}</h3>
        <h3>Gender: ${data[2]}</h3>
        <h3>Date of birth: ${data[3]}</h3>
        <h3>Section: ${data[4]}</h3>
        <h3>Science: ${data[5]}</h3>
        <h3>English: ${data[6]}</h3>
        <h3>History: ${data[7]}</h3>
        <h3>Maths: ${data[8]}</h3>
        <h3>Overall: ${data[9]}</h3>
      `;
    });
  })
</script>
</body>
</html>'''

def generate_report(students):
    print("👩‍🎓👨‍🎓 Summoning the academic spirits to compile the students' report... Expect some magical grades and mystical attendance records! 📜✨")
    # variable which contains final dynamic HTML content
    final_string = ''
    for row in students:
        # variable which contains dynamic HTML content for each row
        rowString = f'<td class="id">{row[0]}</td>'
        for data in row[1:]:
            rowString += f'<td>{data}</td>'
        final_string += f'<tr>{rowString}</tr>'
    report_file = open('report.html', 'w')
    report_file.write(html_template.replace('$$REPLACE_ME$$', final_string))
    report_file.close()
    print("🌟 Voilà! The student report has been magically conjured! Now, let's see who's been a wizard with their studies and who's been dozing in potions class! 📚🔮")
