# -*- coding: utf-8 -*-

from collections import OrderedDict

survey = OrderedDict([
    ("Community Profile", OrderedDict([
        ("Gender", [
            "Female",
            "Male",
            "Other",
            "Prefer not to say"
        ]),
        ("Ethnicity", [
            "Black or of African descent",
            "East Asian",
            "Hispanic or Latino/Latina",
            "Middle Eastern",
            "Native American, Pacific Islander, or Indigenous Australian",
            "South Asian",
            "White or of European descent",
            "Prefer not to say",
            "Other"
        ]),
        ("Highest Educational Attainment", [
            "I never completed any formal education",
            "Primary/elementary school",
            "Secondary school",
            "Some college/university study without earning a bachelor’s degree",
            "Bachelor’s degree",
            "Master’s degree",
            "Professional degree",
            "Doctoral degree",
            "I prefer not to answer"
        ]),
        ("Undergraduate Major", [
            "Art (fine arts or performing arts)",
            "Business",
            "Computer science or software engineering",
            "Computer engineering or electrical/electronics engineering",
            "Computer programming or Web development",
            "Engineering (non computer focused)",
            "Economics",
            "Health science",
            "Humanities",
            "Information technology, networking, or system administration Management information systems",
            "Mathematics or statistics",
            "Natural science",
            "Psychology",
            "Social sciences",
            "I never declared a major",
            "Other"
        ]),
        ("How You Learned to Code", [
            "Bootcamp",
            "Coding competition or part­time course",
            "College",
            "Hackathon",
            "Industry certification",
            "Online course",
            "Open source contributions",
            "Self taught",
            "Other"])
    ])),
    ('Technology', OrderedDict([
        ("Primary Programming Languages Used at Work", [
            "Assembly",
            "C",
            "C++",
            "C#",
            "CoffeeScript",
            "Elixir",
            "Go",
            "Groovy",
            "Haskell",
            "Java",
            "JavaScript",
            "Lua",
            "Matlab",
            "Objective C",
            "PHP",
            "Perl",
            "Python",
            "R",
            "Ruby",
            "Rust",
            "Scala",
            "SQL",
            "Swift",
            "TypeScript",
            "VB",
            ".NET",
            "VBA",
            "Visual Basic 6",
            "Other"
        ]),
        ("Primary Database Technologies Used at Work", [
            "Cassandra",
            "MongoDB",
            "MySQL",
            "Oracle",
            "PostgreSQL",
            "Redis",
            "SQL Server ",
            "SQLite",
            "Other"
        ]),
        ("Primary Platforms Used at Work", [
            "Amazon Web Services (AWS)",
            "Android",
            "Arduino",
            "iOS",
            "Linux Desktop",
            "Mac OS",
            "Mainframe",
            "Microsoft Azure",
            "Raspberry Pi",
            "Salesforce",
            "Serverless",
            "SharePoint",
            "Windows Desktop",
            "Windows Phone",
            "WordPress",
            "Other"
        ]),
        ("Primary Development Environments Used at Work", [
            "Android Studio",
            "Atom",
            "Coda",
            "Eclipse",
            "Emacs",
            "IntelliJ",
            "IPython / Jupyter",
            "Komodo",
            "Light Table",
            "NetBeans",
            "Notepad++",
            "PHPStorm",
            "PyCharm",
            "RStudio",
            "RubyMine",
            "Sublime Text",
            "TextMate",
            "Vim",
            "Visual Studio",
            "Visual Studio Code",
            "Xcode",
            "Zend",
            "Other"
        ]),
        ("Primary Version Control Systems Used at Work", [
            "Git",
            "Mercurial",
            "Subversion",
            "Team Foundation Server",
            "Zip file back­ups",
            "None",
            "Other"
        ])
    ])),
    ("Work", OrderedDict([
        ("Tech Roles", [
            "Consultant (who also writes code)",
            "Consultant (who does NOT write code)",
            "Data Scientist",
            "Database Administrator",
            "Desktop App Developer",
            "Developer with Statistics or Mathematics Background",
            "DevOps Specialist",
            "Embedded Applications/Devices Developer",
            "Graphic Designer",
            "Graphics Programming",
            "Manager (who also writes code)",
            "Manger (who does NOT write code)",
            "Machine Learning Specialist",
            "Mobile Developer",
            "Quality Assurance Engineer",
            "Sales Engineer",
            "Systems Administrator",
            "Web Developer",
            "Other"
            ]),
        ("Years of Professional Experience", range(0, 21)),
        ("Total Compensation", ['${:,}'.format(x) for x in range(5000, 300001, 5000)]),
        ("Satisfaction with Compensation", range(1, 11)),
        ("What You Value Most in Compensation", [
            "Vacation/days off",
            "Remote options",
            "Health benefits",
            "Expected work hours",
            "Equipment",
            "Professional development sponsorship",
            "Annual bonus",
            "Retirement",
            "Education sponsorship",
            "Stock options",
            "Long­term leave",
            "Private office",
            "Child/elder care",
            "Charitable match",
            "Other"
        ]),
        ("How Many Days Per Week You Work From Home", range(0, 8)),
        ("Company Size", ['{} employees'.format(num_range) for num_range in [
            "< 10", "10 - 19", "20 - 99", "100 - 499",
            "500 - 999", "1,000 - 4,999", " 5,000 - 9,999",
            "> 10,000"]]),
        ("How Many Hours You Work Per Week", range(1, 101)),
        ("Work Life Balance", range(1, 11)),
        ("Job Satisfaction", range(1, 11)),
        ("A Customer Calls Late Friday Evening", [
            "I Get on the phone and help. Customer first!",
            "I Let the call go to voice mail. It will be there on Monday",
            "I Call someone else to handle it",
            "I Ignore it"
         ]),
        ("How You Found Your Current Job", [
            "A friend, family member, or former colleague told me",
            "I was contacted directly by someone at the company (e.g. internal recruiter)",
            "A general purpose job board",
            "An external recruiter or headhunter",
            "I visited the company’s Web site and found a job listing there",
            "A career fair or on­campus recruiting event",
            "A tech specific job board",
            "I am the founder",
            "Other"
        ]),
        ("Most Annoying Work Issue", [
            "Office Politics",
            "Bureaucracy",
            "Loud workplace",
            "Overly dependent junior developers",
            "Negligent team leads/Managers",
            "Unhelpful project managers",
            "Unknowledgeable middle management",
            "Unknowledgeable upper management",
            "Always being 'on call'",
            "Long work hours",
            "No natural light",
            "Nothing annoys me at work",
            "Other"
        ]),
        ("Favorite Office Perk", [
            "Ping Pong table",
            "Video games",
            "Board games",
            "Free or discounted food",
            "In office art",
            "Flexible hours",
            "Company Culture",
            "Gym or health reimbursement",
            "Other",
            "Nothing"
        ])
    ])),
    ("Cleveland", OrderedDict([
        ("What Keeps You in Cleveland", [
            "Pro Sports teams",
            "Short commute/lack of traffic",
            "Access to nature (Metroparks, Cuyahoga Nat'l Park)",
            "4 Distinct seasons",
            "Affordable housing/Cost of living",
            "Grew up in Cleveland",
            "Family",
            "Why would I leave the greatest city on Earth?",
            "Work",
            "Other"
        ]),
        ("Favorite Cleveland Pro Sports Team", [
            "Browns",
            "Cavaliers",
            "Indians",
            "Monsters",
            "I don't care about sport ball"
        ]),
        ("Favorite Cleveland Hangout Area", [
            "Coventry Village",
            "Downtown",
            "East Fourth",
            "Edgewater",
            "The Flats",
            "Gordon Square",
            "Lakewood",
            "Little Italy",
            "Ohio City",
            "Playhouse Square",
            "Shaker Square",
            "Slavic Village",
            "Tremont",
            "University Circle",
            "Other"
        ]),
        ("Favorite Cleveland Activity", [
            "A Christmas Story House",
            "Cleveland Botanical Garden",
            "Cleveland Metroparks",
            "Cleveland Metroparks Zoo",
            "Cleveland Museum of Art",
            "Cleveland Museum of Natural History",
            "Cleveland Orchestra at Severance Hall",
            "Great Lakes Science Center",
            "JACK Casino",
            "Lake View Cemetary",
            "Rock & Roll Hall of Fame",
            "USS Cod",
            "West Side Market",
            "Other"
        ])
    ]))
])

# v2 TODO:
# Questions to add to db and edit survey:
# 1. "Satisfaction with Compensation"
# 2. "How Many Hours You Work Per Week"
# 3. "A Customer Calls Late Friday Evening"
# 4. Add comments section to end

labels = [question.replace(' ', '_').lower() for category in survey.keys() for question in survey[category]]

# labels = [question.replace(' ', '_').lower() for question in survey_questions_and_answers.keys()]
# categories = [category for category in survey_questions_and_answers.keys()]
# Community Profile
# Technology
# Work
# Cleveland


# for i, category in enumerate(survey.keys(), 1):
#   print 'Category {}: {}'.format(i, category)
#   for j, question in enumerate(survey[category], 1):
#     print '\t Question {}: {}'.format(i, question)
#     for k, answer in enumerate(survey[category][question], 1):
#       print '\t\t Answer {}: {}'.format(i, answer)
