import tkinter as tk
from tkinter.font import Font
from tkinter import ttk, messagebox
import re

def create_gui():
    global root, feedback_label, frame

    root = tk.Tk()
    root.title("Synbase")
    root.iconbitmap(r'synbaseIcon.ico')

    color1 = '#ef63ff'
    color2 = 'black'



    # Set grey background
    root.configure(bg='#121212')

    # Create scrollable frame
    canvas = tk.Canvas(root, bg='#121212', highlightthickness=0)
    frame = tk.Frame(canvas, bg='#121212', bd=10)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Add scrollable frame to canvas
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Pre-determined values for the boxes
    box_values = [
        {"name": "TechEdu Solutions", "website": "www.techedusolutions.com", "contact": "Sarah Anderson", "email": "sarah@techedusolutions.com", "phone": "555-123-4567", "description": "TechEdu Solutions provides comprehensive technology solutions for CTE programs, including virtual labs, interactive learning platforms, and student assessment tools."},
        {"name": "InnoSkillsTech", "website": "www.innoskillstech.io", "contact": "Michael Carter", "email": "michael@innoskillstech.io", "phone": "555-234-5678", "description": "InnoSkillsTech specializes in developing cutting-edge skill assessment software, helping CTE directors track student progress and tailor their programs to individual needs."},
        {"name": "VirtuLearn Systems", "website": "www.virtulearnsystems.com", "contact": "Emily Rodriguez", "email": "emily@virtulearnsystems.com", "phone": "555-345-6789", "description": "VirtuLearn Systems offers virtual reality (VR) educational experiences for CTE programs, enhancing hands-on learning in a simulated environment."},
        {"name": "EduTrack Innovations", "website": "www.edutrackinnovations.net", "contact": "Jason Turner", "email": "jason@edutrackinnovations.net", "phone": "555-456-7890", "description": "EduTrack Innovations provides a comprehensive tracking and reporting system, allowing CTE directors to monitor student performance and program effectiveness."},
        {"name": "CodeCrafters", "website": "www.codecrafters.com", "contact": "Lisa Johnson", "email": "lisa@codecrafters.com", "phone": "555-567-8901", "description": "CodeCrafters specializes in coding and programming resources for CTE programs, offering a platform for students to develop technical skills."},
        {"name": "SimuSkill Technologies", "website": "www.simuskilltech.co", "contact": "Ryan Miller", "email": "ryan@simuskilltech.co", "phone": "555-678-9012", "description": "SimuSkill Technologies provides realistic simulation software for CTE programs, allowing students to practice skills in a risk-free virtual environment."},
        {"name": "TechTutorHub", "website": "www.techtutorhub.com", "contact": "Jessica Lee", "email": "jessica@techtutorhub.com", "phone": "555-789-0123", "description": "TechTutorHub offers a comprehensive online tutoring platform, connecting CTE students with experienced industry professionals for personalized guidance."},
        {"name": "SkillForge Solutions", "website": "www.skillforge.net", "contact": "Brian Adams", "email": "brian@skillforge.net", "phone": "555-890-1234", "description": "SkillForge Solutions provides skill development programs for CTE, offering a range of courses in areas such as IT, healthcare, and engineering."},
        {"name": "EduTech Innovators", "website": "www.edutechinnovators.org", "contact": "Megan Taylor", "email": "megan@edutechinnovators.org", "phone": "555-901-2345", "description": "EduTech Innovators focuses on integrating the latest educational technologies into CTE programs, enhancing the learning experience for students."},
        {"name": "DigitalDesign Pro", "website": "www.digitaldesignpro.com", "contact": "Eric Chang", "email": "eric@digitaldesignpro.com", "phone": "555-012-3456", "description": "DigitalDesign Pro offers graphic design and multimedia tools tailored for CTE programs, empowering students to unleash their creativity."},
        {"name": "RoboWorks Industries", "website": "www.roboworksindustries.com", "contact": "Rachel Simmons", "email": "rachel@roboworksindustries.com", "phone": "555-123-4567", "description": "RoboWorks Industries specializes in robotics education, providing kits and software for hands-on learning in STEM-focused CTE programs."},
        {"name": "DataDive Analytics", "website": "www.datadiveanalytics.com", "contact": "Kevin Wilson", "email": "kevin@datadiveanalytics.com", "phone": "555-234-5678", "description": "DataDive Analytics offers data analysis tools and training for CTE programs, preparing students for careers in data science and analytics."},
        {"name": "CyberGuard Systems", "website": "www.cyberguardsystems.com", "contact": "Angela Martinez", "email": "angela@cyberguardsystems.com", "phone": "555-345-6789", "description": "CyberGuard Systems provides cybersecurity education solutions, including simulations and training modules for CTE programs."},
        {"name": "FutureBuilders Tech", "website": "www.futurebuilderstech.org", "contact": "Daniel Parker", "email": "daniel@futurebuilderstech.org", "phone": "555-456-7890", "description": "FutureBuilders Tech focuses on emerging technologies, offering CTE programs resources to explore innovations in AI, blockchain, and more."},
        {"name": "SkillSync Academy", "website": "www.skillsyncacademy.com", "contact": "Michelle Carter", "email": "michelle@skillsyncacademy.com", "phone": "555-567-8901", "description": "SkillSync Academy provides synchronized learning experiences, integrating real-world projects into CTE curriculum to enhance practical skills."},
        {"name": "TechHub Connect", "website": "www.techhubconnect.net", "contact": "Jonathan Baker", "email": "jonathan@techhubconnect.net", "phone": "555-678-9012", "description": "TechHub Connect offers a collaborative platform for CTE programs, facilitating communication and resource sharing among educators and students."},
        {"name": "InnoTech Solutions", "website": "www.innotechsolutions.com", "contact": "Michelle Chang", "email": "michelle@innotechsolutions.com", "phone": "555-123-4567", "description": "InnoTech Solutions specializes in innovative software solutions for businesses, optimizing processes and enhancing productivity."},
        {"name": "EcoGrowth Ventures", "website": "www.ecogrowthventures.com", "contact": "Alex Rodriguez", "email": "alex@ecogrowthventures.com", "phone": "555-987-6543", "description": "EcoGrowth Ventures is dedicated to promoting sustainable practices, offering eco-friendly products and consulting services for businesses seeking to go green."},
        {"name": "TechInnovate Solutions", "website": "www.techinnovatesolutions.com", "contact": "Alexandra Smith", "email": "alexandra@techinnovatesolutions.com", "phone": "555-789-0123", "description": "TechInnovate Solutions pioneers innovative technology solutions for CTE programs, offering a wide range of cutting-edge tools and platforms to enhance the learning experience for students."},
        {"name": "HealthHub Technologies", "website": "www.healthhubtech.com", "contact": "Dr. Kevin Patel", "email": "kevin@healthhubtech.com", "phone": "555-234-5678", "description": "HealthHub Technologies leverages cutting-edge technology to improve healthcare outcomes, offering solutions for patient engagement and remote monitoring."},
        {"name": "FutureFarm Innovations", "website": "www.futurefarminnovations.com", "contact": "Sarah Mitchell", "email": "sarah@futurefarminnovations.com", "phone": "555-345-6789", "description": "FutureFarm Innovations pioneers smart agriculture solutions, integrating technology to enhance crop yields and sustainability."},
        {"name": "NanoTech Dynamics", "website": "www.nanotechdynamics.com", "contact": "Dr. Michael Wong", "email": "michael@nanotechdynamics.com", "phone": "555-876-5432", "description": "NanoTech Dynamics specializes in nanotechnology research and development, creating innovative solutions for various industries."},
        {"name": "SkyLink Robotics", "website": "www.skylinkrobotics.com", "contact": "Lisa Taylor", "email": "lisa@skylinkrobotics.com", "phone": "555-567-8901", "description": "SkyLink Robotics designs and manufactures cutting-edge robotic systems for industrial automation and exploration."},
        {"name": "FinanceFleet Solutions", "website": "www.financefleet.com", "contact": "David Reynolds", "email": "david@financefleet.com", "phone": "555-678-9012", "description": "FinanceFleet Solutions offers comprehensive financial management tools for businesses, optimizing budgeting and expense tracking."},
        {"name": "SolarCraft Innovations", "website": "www.solarcraftinnovations.com", "contact": "Sophie Reynolds", "email": "sophie@solarcraftinnovations.com", "phone": "555-567-8901", "description": "SolarCraft Innovations harnesses solar energy for sustainable solutions, offering solar power systems and consulting services."}
    ]

    # Add boxes to the frame
    for values in box_values:
        box_frame = create_box(frame, values)
        box_frame.pack(pady=10)

    # Add search feature
    search_label = tk.Label(root, text="Search:", font=('Arial', 14), bg='#121212', fg='white')
    search_label.pack(pady=5)
    search_entry = tk.Entry(root, font=('Arial', 14), bd=5, highlightthickness=2, highlightbackground=color2, highlightcolor=color1, width=13, border=0)
    search_entry.pack(pady=5)
    search_button = tk.Button(root, text="Search", command=lambda: search_boxes(frame, box_values, search_entry.get()), font=('Arial', 14), bd=5, foreground=color1, background=color2, activebackground=color1, activeforeground=color2, highlightthickness=2, highlightbackground=color2, highlightcolor=color1, width=13, height=2, border=0, cursor="hand1")
    search_button.pack(pady=10)

    # Add create button
    create_button = tk.Button(root, text="Create", command=lambda: create_new_box(frame, box_values), font=('Arial', 14), bd=5, foreground=color1, background=color2, activebackground=color1, activeforeground=color2, highlightthickness=2, highlightbackground=color2, highlightcolor=color1, width=13, height=2, border=0, cursor="hand1")
    create_button.pack(pady=10)

    # Add sorting button with popup
    sort_button = tk.Button(root, text="Sort", command=lambda: show_sort_popup(sort_boxes, frame, box_values), font=('Arial', 14), bd=5, foreground=color1, background=color2, activebackground=color1, activeforeground=color2, highlightthickness=2, highlightbackground=color2, highlightcolor=color1, width=13, height=2, border=0, cursor="hand1")
    sort_button.pack(pady=10)

    # Add chatbot entry and button
    chatbot_entry = tk.Entry(root, font=('Arial', 14), bd=5, highlightthickness=2, highlightbackground=color2, highlightcolor=color1, width=13, border=0)
    chatbot_entry.pack(pady=5)

    chatbot_button = tk.Button(root, text="Ask Chatbot", command=lambda: ask_chatbot(chatbot_entry.get()), font=('Arial', 14), bd=5, foreground=color1, background=color2, activebackground=color1, activeforeground=color2, highlightthickness=2, highlightbackground=color2, highlightcolor=color1, width=13, height=2, border=0, cursor="hand1")
    chatbot_button.pack(pady=10)

    # Configure canvas scrolling
    frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))

    # Bind mousewheel to scroll
    root.bind_all("<MouseWheel>", lambda event, canvas=canvas: on_mousewheel(event, canvas))

    feedback_label = tk.Label(root, text="", font=('Arial', 12), fg='green', bg='#121212')
    feedback_label.pack(pady=20)

    root.mainloop()

# ... (rest of the code remains unchanged)


    root.mainloop()

def create_box(parent, values):
    box_frame = tk.Frame(parent, bg='white', highlightbackground="#1E1E1E", highlightthickness=1, relief=tk.RIDGE, bd=5)
    name_label = tk.Label(box_frame, text="Name: " + values["name"], font=('Arial', 12), bg='white')
    website_label = tk.Label(box_frame, text="Website: " + values["website"], font=('Arial', 12), bg='white')
    contact_label = tk.Label(box_frame, text="Contact: " + values["contact"], font=('Arial', 12), bg='white')
    email_label = tk.Label(box_frame, text="Email: " + values["email"], font=('Arial', 12), bg='white')
    phone_label = tk.Label(box_frame, text="Phone: " + values["phone"], font=('Arial', 12), bg='white')
    description_label = tk.Label(box_frame, text="Description: " + values["description"], font=('Arial', 12), bg='white', wraplength=400)

    name_label.pack(anchor="w")
    website_label.pack(anchor="w")
    contact_label.pack(anchor="w")
    email_label.pack(anchor="w")
    phone_label.pack(anchor="w")
    description_label.pack(anchor="w")

    return box_frame

def create_new_box(parent, box_values):
    # Create a popup window for user input
    popup = tk.Toplevel()
    popup.title("Create New Box")

    # Create entry widgets for each field
    name_entry = tk.Entry(popup, font=('Arial', 12), bd=5)
    website_entry = tk.Entry(popup, font=('Arial', 12), bd=5)
    contact_entry = tk.Entry(popup, font=('Arial', 12), bd=5)
    email_entry = tk.Entry(popup, font=('Arial', 12), bd=5)
    phone_entry = tk.Entry(popup, font=('Arial', 12), bd=5)
    description_entry = tk.Entry(popup, font=('Arial', 12), bd=5)

    # Create labels for each entry
    name_label = tk.Label(popup, text="Name:", font=('Arial', 12))
    website_label = tk.Label(popup, text="Website:", font=('Arial', 12))
    contact_label = tk.Label(popup, text="Contact:", font=('Arial', 12))
    email_label = tk.Label(popup, text="Email:", font=('Arial', 12))
    phone_label = tk.Label(popup, text="Phone:", font=('Arial', 12))
    description_label = tk.Label(popup, text="Description:", font=('Arial', 12))

    # Create a feedback label for validation messages
    feedback_label = tk.Label(popup, text="", font=('Arial', 12), fg='red')
    feedback_label.grid(row=6, column=0, columnspan=2, pady=5)

    # Create a function to add the new box to the list and close the popup
    def add_box():
        nonlocal parent

        # Validate entries
        if not all((name_entry.get(), website_entry.get(), contact_entry.get(), email_entry.get(), phone_entry.get(), description_entry.get())):
            feedback_label["text"] = "Please fill in all fields"
            feedback_label["fg"] = "red"
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_entry.get()):
            feedback_label["text"] = "Invalid email format"
            feedback_label["fg"] = "red"
            return

        if not phone_entry.get().isdigit():
            feedback_label["text"] = "Phone number must contain only numbers"
            feedback_label["fg"] = "red"
            return

        # Create a dictionary with the new box values
        new_box = {
            "name": name_entry.get(),
            "website": website_entry.get(),
            "contact": contact_entry.get(),
            "email": email_entry.get(),
            "phone": phone_entry.get(),
            "description": description_entry.get()
        }

        # Add the new box to the list
        box_values.append(new_box)

        # Close the popup
        popup.destroy()

        # Refresh the GUI with the new box
        refresh_gui(parent, box_values)

        # Display success message
        feedback_label["text"] = "Box added successfully"
        feedback_label["fg"] = "green"

    # Create a button to add the new box
    add_button = tk.Button(popup, text="Add Box", command=add_box, font=('Arial', 12), bd=5)
    add_button.grid(row=7, column=0, pady=10, sticky="w")

    # Create a button to cancel the operation
    cancel_button = tk.Button(popup, text="Cancel", command=popup.destroy, font=('Arial', 12), bd=5)
    cancel_button.grid(row=7, column=1, pady=10, sticky="e")

    # Arrange entry widgets and labels in a grid
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    website_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    website_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    contact_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    contact_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    email_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    email_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    phone_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
    phone_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")
    description_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
    description_entry.grid(row=5, column=1, padx=5, pady=5, sticky="w")

def refresh_gui(parent, box_values):
    # Destroy all widgets in the frame
    for widget in parent.winfo_children():
        widget.destroy()

    # Add boxes to the frame
    for values in box_values:
        box_frame = create_box(parent, values)
        box_frame.pack(pady=10)

def search_boxes(parent, box_values, query):
    # Clear existing boxes from the frame
    for widget in parent.winfo_children():
        widget.destroy()

    # Filter boxes based on the search query
    matching_boxes = [values for values in box_values if query.lower() in values["name"].lower()]

    # Add matching boxes to the frame
    for values in matching_boxes:
        box_frame = create_box(parent, values)
        box_frame.pack(pady=10)

def sort_boxes(parent, box_values, key_function, reverse=False):
    # Sort box_values based on the key_function
    sorted_boxes = sorted(box_values, key=key_function, reverse=reverse)

    # Clear existing boxes from the frame
    for widget in parent.winfo_children():
        widget.destroy()

    # Add sorted boxes to the frame
    for values in sorted_boxes:
        box_frame = create_box(parent, values)
        box_frame.pack(pady=10)

def show_sort_popup(sort_function, parent, box_values):
    # Create a popup window for sorting options
    sort_popup = tk.Toplevel()
    sort_popup.title("Sort Options")

    # Create labels and buttons for each sorting option
    asc_name_button = tk.Button(sort_popup, text="Sort by Name (Ascending)", command=lambda: sort_function(parent, box_values, key_function=lambda x: x["name"]))
    desc_name_button = tk.Button(sort_popup, text="Sort by Name (Descending)", command=lambda: sort_function(parent, box_values, key_function=lambda x: x["name"], reverse=True))

    asc_name_button.pack(pady=10)
    desc_name_button.pack(pady=10)

def ask_chatbot(question):
    # Fill in your predefined question-response pairs in the 'responses' dictionary
    responses = {
        "What services does Techedu Solutions provide": "TechEdu Solutions provides comprehensive technology solutions for CTE programs, including virtual labs, interactive learning platforms, and student assessment tools",
        "tell me about innoskillstech": "InnoSkillsTech specializes in developing cutting-edge skill assessment software, helping CTE directors track student progress and tailor their programs to individual needs",
        "hi": "Hello! How can I help you today",
        "bye": "Goodbye! Feel free to return if you have more questions",
        "what is the contact information for virtulearn systems": "You can contact VirtuLearn Systems through Emily Rodriguez at emily@virtulearnsystems.com or by phone at 555-345-6789",
        "can you provide details about edutech innovations": "EduTech Innovations focuses on integrating the latest educational technologies into CTE programs, enhancing the learning experience for students",
        "give me information about codecrafters": "CodeCrafters specializes in coding and programming resources for CTE programs, offering a platform for students to develop technical skills",
        "tell me about the services of cyberguard systems": "CyberGuard Systems provides cybersecurity education solutions, including simulations and training modules for CTE programs",
        "what does futurebuilders tech focus on": "FutureBuilders Tech focuses on emerging technologies, offering CTE programs resources to explore innovations in AI, blockchain, and more",
        "what is the purpose of skillsync academy": "SkillSync Academy provides synchronized learning experiences, integrating real-world projects into CTE curriculum to enhance practical skills",
        "what does techhub connect offer": "TechHub Connect offers a collaborative platform for CTE programs, facilitating communication and resource sharing among educators and students",
        "how can i contact digitaldesign pro": "You can contact DigitalDesign Pro through Eric Chang at eric@digitaldesignpro.com or by phone at 555-012-3456",
        "what does roboworks industries specialize in": "RoboWorks Industries specializes in robotics education, providing kits and software for hands-on learning in STEM-focused CTE programs",
        "can you provide details about the contact person for virtulearn systems": "The contact person for VirtuLearn Systems is Emily Rodriguez You can reach her at emily@virtulearnsystems.com or by phone at 555-345-6789",
        "how can i get more information about innoskillstech": "You can get more information about InnoSkillsTech on their website at www.innoskillstech.io or by contacting Michael Carter at michael@innoskillstech.io",
        "tell me about the phone number for edutech innovations": "The phone number for EduTech Innovations is 555-901-2345",
        "what is the email address for codecrafters": "The email address for CodeCrafters is lisa@codecrafters.com",
        "how can i contact cyberguard systems": "You can contact CyberGuard Systems through Angela Martinez at angela@cyberguardsystems.com or by phone at 555-345-6789",
        "give me information about the website of datadive analytics": "The website for DataDive Analytics is www.datadiveanalytics.com",
        "what does futurebuilders tech offer": "FutureBuilders Tech focuses on emerging technologies, offering CTE programs resources to explore innovations in AI, blockchain, and more",
        "how can i reach skillsync academy": "You can reach SkillSync Academy by contacting Michelle Carter at michelle@skillsyncacademy.com or by phone at 555-567-8901",
        "what services does techhub connect provide": "TechHub Connect offers a collaborative platform for CTE programs, facilitating communication and resource sharing among educators and students",
        "tell me about the phone number for virtulearn systems": "The phone number for VirtuLearn Systems is 555-678-9012",
        "what is the contact information for digitaldesign pro": "You can contact DigitalDesign Pro through Eric Chang at eric@digitaldesignpro.com or by phone at 555-012-3456",
        "can you provide details about roboworks industries": "RoboWorks Industries specializes in robotics education, providing kits and software for hands-on learning in STEM-focused CTE programs",
        "give me information about the email address of edutrack innovations": "The email address for EduTrack Innovations is jason@edutrackinnovations.net",
        "what is the website of techedu solutions": "The website for TechEdu Solutions is www.techedusolutions.com",
        "tell me about the email address of innoskillstech": "The email address for InnoSkillsTech is michael@innoskillstech.io",
        "what is the phone number for virtulearn systems": "The phone number for VirtuLearn Systems is 555-345-6789",
        "how can i contact edutech innovators": "You can contact EduTech Innovators through Megan Taylor at megan@edutechinnovators.org or by phone at 555-901-2345",
        "tell me about the website of codecrafters": "The website for CodeCrafters is www.codecrafters.com",
        "what services does simuskill technologies provide": "SimuSkill Technologies provides realistic simulation software for CTE programs, allowing students to practice skills in a risk-free virtual environment",
        "can you provide details about the contact person for techtutorhub": "The contact person for TechTutorHub is Jessica Lee You can reach her at jessica@techtutorhub.com or by phone at 555-789-0123",
        "give me information about the phone number of skillforge solutions": "The phone number for SkillForge Solutions is 555-890-1234",
        "what is the email address for edutech innovators": "The email address for EduTech Innovators is megan@edutechinnovators.org",
        "how can i contact virtulearn systems": "You can contact VirtuLearn Systems through Emily Rodriguez at emily@virtulearnsystems.com or by phone at 555-345-6789",
        "tell me about the services of codecrafters": "CodeCrafters specializes in coding and programming resources for CTE programs, offering a platform for students to develop technical skills"
    }

    # Clean the question by removing extra spaces, commas, and converting to lowercase
    cleaned_question = re.sub(r'[^a-zA-Z0-9 ]', '', question.lower())

    # Check if the cleaned question has a predefined response
    response = responses.get(cleaned_question, "I'm sorry, I don't have information on that.")

    # Display the chatbot response in the feedback label
    feedback_label["text"] = response
    feedback_label["fg"] = "black"



def on_frame_configure(canvas):
    # Update scrollregion when the size of the frame changes
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel(event, canvas):
    # Scroll up or down based on the mouse wheel movement
    if event.delta < 0:
        canvas.yview_scroll(1, "units")
    else:
        canvas.yview_scroll(-1, "units")

# Run the GUI
create_gui()
