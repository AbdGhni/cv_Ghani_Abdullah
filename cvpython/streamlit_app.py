import streamlit as st
from PIL import Image


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Ghani Abdullah, Data and IA Engineer student.
##### *Resume* 
''')

image = Image.open('dp.png')
st.image(image, width=170)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- A third-year engineering student at ECE Paris, majoring in Data and AI, seeking a 2 to 3-year apprenticeship.
- Strong verbal and written communication skills, Good analytical thinking.
- Proficient in Python, Excel, Word, and much more.
        ''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Ghani Abdullah</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#academic-projects">Academics Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#computer-skills">Computer Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#languages">Languages</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#interests">Interests</a>
      <li class="nav-item">
        <a class="nav-link" href="#github">GitHub</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelor of Medicine**, *Sorbonne Paris-Nord Université*, France',
'2019-2021')

txt('**Bachelors of Science** (Physical and Mathematical science), *Université Paris Saclay*, France',
'2022-2024 ')
st.markdown('''
- GPA: `4,0`(16.09/20)
- Graduated with First Class Honors.
- I was part of the elite mathematics class.
''')

txt('**Engineering school** (Data,AI,IT/IS,Cybersecurity), *ECE Paris*, France',
'2024-2027')
#####################
st.markdown('''
## Work Experience
''')

txt('**Math and Physics-Chemistry Tutor**, EURÊKA, France',
'Since 2021')
st.markdown('''
-Teaching mathematics and physics-chemistry to classes of students from middle school to high school.
''')

txt('**Private Tutor in Mathematics and Physics**,Self-employed, Paris, France',
'2012-2021')
st.markdown('''
-Provided personalized instruction in mathematics and physics to students from 8th grade to 12th grade.
''')

txt('**Logistics**, LA POSTE ,Roissy Charles de Gaulle',
'2021-2023')

st.markdown('''
## Certifications
''')
st.markdown('''
- Azure Data Fundamentals
- Azure AI Fundamentals
- EUGLOH- Intercultural Communication
''')

#####################
st.markdown('''
## Academic Projects
''')

txt('**Creation of a Cellular Automaton**','Turing-complete')
st.markdown('''
- Developed a cellular automaton that meets the criteria for Turing completeness.
- Simulated John Horton Conway's "Game of Life."
- Fully coded in Python.
''')

txt('**Creation of a Video Game in Python**','Pong,Breakout...')
st.markdown('''
- Utilized the Pygame library for game development.
- Implemented a graphical user interface using Tkinter.
''')

txt('**Logistics**, LA POSTE ,Roissy Charles de Gaulle',
'2021-2023')


st.markdown('''
## Computer Skills
''')
st.markdown('''
- Python
- Excel
- PackOffice
- GeoGebra            
''')

st.markdown('''
## Languages
''')
st.markdown('''
- French: Native speaker
- Hindi: Native speaker
- English: C1
- Spanish: B2
- Urdu: Native speaker         
''')

st.markdown('''
## Interests
''')
st.markdown('''
- Karate Club
- Rugby Club: Number 2, Hooker
- Theater Club: Lead role in the play "The Little Prince"        
''')

st.markdown('''
## GitHub
''')
st.markdown('''
- https://github.com/AbdGhni/Python-Projects
            ''')