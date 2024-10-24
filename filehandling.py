import os
# file = open("FamilyLineage.txt",'w')
# file.write(" Biplav Karki, Sribika B. Karki, Bishal Karki, Bindu Karki, Bivek C. Karki")
# file.close()

# readfile = open("FamilyLineage.txt",'r')
# content = readfile.read()
# print(content)
# readfile.close()  

text = ''' Lorem  ipsum dolor sit amet,  consectetur adipiscing elit.   

Nullam  tincidunt, orci nec  laoreet  posuere,  lectus   felis  aliquet  ligula, a   efficitur  arcu   odio in libero. Sed  varius,  nisl sit  amet  bibendum    bibendum,   elit   dui  scelerisque nunc,   ac   fermentum massa   nisi  at   ipsum.   

Cras   malesuada     mi  sed  sem   gravida, ac tempor   justo  varius. Vivamus    sit  amet    justo  id  urna  facilisis  suscipit.  Aenean    ut  felis    ut  urna aliquet      cursus. 

Sed  ut enim   eget  ligula   scelerisque sollicitudin.   Donec    blandit   faucibus  odio, at dictum   nulla consequat  eu. 

Nam   euismod    elit   vel    luctus  tincidunt,  libero  turpis  scelerisque eros,   ac sagittis  quam  nisi  id  risus.   Curabitur   lacinia   turpis   eu  gravida  finibus. 
    '''
cleaned_lines = []
for t in text.splitlines():
    cleaned_line = '-'.join(t.strip().split())
    if cleaned_line: 
        cleaned_lines.append(cleaned_line)
final_text = ''.join(cleaned_lines)
filename = "FamilyLineage.txt"
if os.path.exists(filename):
    with open(filename,'a') as file:
        file.write('\n' + final_text)
else:
    with open(filename,'w') as file:
        file.write(final_text)

with open(filename,'r') as readfile:
    content=readfile.readlines()

    for c in content:
        print(c.replace('-',' '))



    

