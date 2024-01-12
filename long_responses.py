import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

R_COURSE_INFO="In CSE following specialization are being offered:\nInternet of Things & Cyber Security including Blockchain Technology\nCybersecurity,Artificial Intelligence\nMachine Learning and Artificial Intelligence\nAl and Data Science"

R_LABS=" The department provides a state-of-the-art infrastructure, equipped with the latest hardware and software. A few examples are the CISCO Networking Academy launched in collaboration with CISCO, the Ubuntu Lab, the IoT lab, and MAC Computer Center."

R_PLACEMENT="Graphic Era has consistently set benchmarks in the region for Placements across Top MNCs globally, and the Year 2023 has been no different. Our students have aced the toughest of the selection processes and joined their dream companies at some of the highest packages in the country. "

R_CURRICULUM="B.Tech CSE is a 4-year undergraduate degree program that focuses on the application and principles of computer science and engineering. Students learn about various aspects of computer science such as software development, programming, data structures, algorithms, computer networks, cybersecurity, artificial intelligence, and more. "

R_FACULTY="There are profound faculty members like Prof. (Dr.) Sanjay Jasola(Professor)\nDr. Vrince Vimal(Professor)\nDr. Mahesh Manchanda(Professor) and many more."

R_VICE_CHANCELLOR="Prof. Sanjay Jasola is currently the Vice Chancellor of Graphic Era Hill University. He served as the founding Vice Chancellor from November 2011 to November 2021 and later as Director General from Nov 2021 to May 2023. With three decades of experience in teaching, research, and academic administration, he was previously Dean at Gautam Buddha University, Greater NOIDA, and a faculty member at Wawasan Open University, Penang, Malaysia.Prof. Jasola holds a B.Tech in Computer Science and Engineering from KNIT Sultanpur, an M.Tech in Computer Science and Technology from IIT Roorkee, and a Ph.D. in Computer Science from Jawaharlal Nehru University, New Delhi. He has published over 80 papers, guided 21 M.Tech and 3 Ph.D. students, and received the Gold Medal for Innovation in Open & Distance Learning from IGNOU. Under his leadership, Graphic Era Hill University has been a pioneer in integrating MOOCs into its curriculum since 2014."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "What does that mean?"][
        random.randrange(3)]
    return response