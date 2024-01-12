# We will be utilizing the package "Gooey" in order to develop the UI of the program
from gooey import Gooey, GooeyParser
from argparse import ArgumentParser


# Values which will be utilized for each company
company_values = [
    {"name": "TechEdu Solutions", "website": "www.techedusolutions.com", "contact": "Sarah Anderson", "email": "sarah@techedusolutions.com", "phone": "555-123-4567", "description": "TechEdu Solutions provides comprehensive technology solutions for CTE programs, including virtual labs, interactive learning platforms, and student assessment tools."},
    {"name": "InnoSkillsTech", "website": "www.innoskillstech.io", "contact": "Michael Carter", "email": "michael@innoskillstech.io", "phone": "555-234-5678", "description": "InnoSkillsTech specializes in developing cutting-edge skill assessment software, helping CTE directors track student progress and tailor their programs to individual needs."},
    {"name": "VirtuLearn Systems", "website": "www.virtulearnsystems.com", "contact": "Emily Rodriguez", "email": "emily@virtulearnsystems.com", "phone": "555-345-6789", "description": "VirtuLearn Systems offers virtual reality (VR) educational experiences for CTE programs, enhancing hands-on learning in a simulated environment."},
    {"name": "EduTrack Innovations", "website": "www.edutrackinnovations.net", "contact": "Jason Turner", "email": "jason@edutrackinnovations.net", "phone": "555-456-7890", "description": "EduTrack Innovations provides a comprehensive tracking and reporting system, allowing CTE directors to monitor student performance and program effectiveness."},
    {"name": "CodeCrafters", "website": "www.codecrafters.com", "contact": "Lisa Johnson", "email": "lisa@codecrafters.com", "phone": "555-567-8901", "description": "CodeCrafters specializes in coding and programming resources for CTE programs, offering a platform for students to develop technical skills."},        {"name": "SimuSkill Technologies", "website": "www.simuskilltech.co", "contact": "Ryan Miller", "email": "ryan@simuskilltech.co", "phone": "555-678-9012", "description": "SimuSkill Technologies provides realistic simulation software for CTE programs, allowing students to practice skills in a risk-free virtual environment."},
    {"name": "TechTutorHub", "website": "www.techtutorhub.com", "contact": "Jessica Lee", "email": "jessica@techtutorhub.com", "phone": "555-789-0123", "description": "TechTutorHub offers a comprehensive online tutoring platform, connecting CTE students with experienced industry professionals for personalized guidance."},        {"name": "SkillForge Solutions", "website": "www.skillforge.net", "contact": "Brian Adams", "email": "brian@skillforge.net", "phone": "555-890-1234", "description": "SkillForge Solutions provides skill development programs for CTE, offering a range of courses in areas such as IT, healthcare, and engineering."},
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

# Function used to display searched boxes
def display_matching_boxes(query):
    matching_boxes = [values for values in company_values if query.lower() in values["name"].lower()]
    # Creates a list of relative boxes which match the search
    if matching_boxes:
        for values in matching_boxes:
            print(f"Name: {values['name']}")
            print(f"Website: {values['website']}")
            print(f"Contact: {values['contact']}")
            print(f"Email: {values['email']}")
            print(f"Phone: {values['phone']}")
            print(f"Description: {values['description']}")
            print("-" * 30)
    else:
        print("No matching boxes found.")

# Function used to display boxes in UI by themselves
def display_companies_standalone():
    for values in company_values:
        print(f"Name: {values['name']}")
        print(f"Website: {values['website']}")
        print(f"Contact: {values['contact']}")
        print(f"Email: {values['email']}")
        print(f"Phone: {values['phone']}")
        print(f"Description: {values['description']}")
        print("-" * 30)
    

# UI Customization
@Gooey(
    program_name="CTE Program Management System",
    program_description="Vihaan Gowda, Vishal Naveen, Aditya Shukla",
    body_bg_color='#292727',
    header_bg_color="#1E1E1E",
    footer_bg_color="#292727",
    terminal_panel_color = "#292727",
    terminal_font_color = "#FFFFFF",
    tabbed_groups=False,
    advanced=True,
    monospace_display=True,
    body_font_color = "White",
    clear_before_run = True,
    menu=[
        {'name': 'Program Information', 'items': [
            {'type': 'AboutDialog', 'menuTitle': 'About This Program', 'name': 'CTE Program Management System',
             'description': 'Vihaan Gowda, Vishal Naveen, Aditya Shukla'},
            {'type': 'Link', 'menuTitle': 'Source Code', 'url': 'https://github.com/VihaanGowda/ctecareerandtechnicaldatabase/tree/main'},
        ]},
    ]
)
def main():
    parser = GooeyParser()
    # Defining the filter box
    filter_group = parser.add_argument_group(
        "Filter Settings",
        "Filter Partner Information"
    )
    add_group = parser.add_argument_group(
        "Add Partner Corporation/Group"
        
    )
    filter_group.add_argument("Search", help="*Currently Functional For Company Names*", default=None, widget="TextField", nargs = "?")
    filter_group.add_argument("option", choices=["Sort A-Z", "Sort Z-A"], metavar="Sorting", help="Sorting our businesses", default=None, widget="Dropdown", nargs="?")
    
    add_group.add_argument("Name", help="Name of the Organization", action="store", nargs = "?")
    add_group.add_argument("Website", help="Name of the Organization", action="store", nargs = "?")
    add_group.add_argument("Contact", help="Name of the Organization", action="store", nargs = "?")
    add_group.add_argument("Email", help="Name of the Organization", action="store", nargs = "?")
    add_group.add_argument("Phone", help="Name of the Organization", action="store", nargs = "?")
    add_group.add_argument("Description", help="Name of the Organization", action="store", nargs = "?")
    
    
    args = parser.parse_args()
    search_query = args.Search
    
    # Append new company
    new_company = {"name": args.Name, "website": args.Website, "contact": args.Contact, "email": args.Email, "phone": args.Phone, "description": args.Description}

    if args.Search is not None:
        display_matching_boxes(search_query)
    elif args.Search is None:
        display_companies_standalone()
    else:
        print("Please Re-Load the Program")
        


        

   

main()
