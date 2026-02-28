# ==============================
# Lead Dataset
# ==============================

leads = [
    {"source": "LinkedIn", "status": "New", "title": "Data Analyst", "course": "Advanced SQL & Python", "created_date": "15-02-26"},
    {"source": "Organic Search", "status": "Contacted", "title": "Software Engineer", "course": "Full-Stack Development", "created_date": "16-02-26"},
    {"source": "Referral", "status": "Qualified", "title": "Project Manager", "course": "Agile Methodologies", "created_date": "16-02-26"},
    {"source": "Facebook Ads", "status": "New", "title": "Marketing Specialist", "course": "Digital Growth Hacking", "created_date": "17-02-26"},
    {"source": "Webinar", "status": "Nurturing", "title": "Student", "course": "Introduction to Machine Learning", "created_date": "17-02-26"},
    {"source": "LinkedIn", "status": "Unqualified", "title": "HR Manager", "course": "Data Visualization", "created_date": "18-02-26"},
    {"source": "Direct Traffic", "status": "Converted", "title": "Freelance Designer", "course": "UI/UX Design Masterclass", "created_date": "18-02-26"},
    {"source": "Google Ads", "status": "New", "title": "Business Analyst", "course": "Tableau for Beginners", "created_date": "19-02-26"},
    {"source": "Organic Search", "status": "Nurturing", "title": "Systems Admin", "course": "Cloud Architecture (AWS)", "created_date": "19-02-26"},
    {"source": "Referral", "status": "Contacted", "title": "Product Owner", "course": "Scrum Certification", "created_date": "20-02-26"},
    {"source": "LinkedIn", "status": "Qualified", "title": "Junior Developer", "course": "React & Next.js", "created_date": "20-02-26"},
    {"source": "Twitter", "status": "New", "title": "Content Creator", "course": "Video Editing Pro", "created_date": "21-02-26"},
    {"source": "Webinar", "status": "New", "title": "Operations Lead", "course": "Lean Six Sigma", "created_date": "21-02-26"},
    {"source": "Facebook Ads", "status": "Unqualified", "title": "Retail Associate", "course": "Cybersecurity Fundamentals", "created_date": "22-02-26"},
    {"source": "Direct Traffic", "status": "Converted", "title": "Backend Dev", "course": "Go Programming", "created_date": "22-02-26"},
    {"source": "LinkedIn", "status": "Nurturing", "title": "Data Scientist", "course": "Deep Learning Specialization", "created_date": "23-02-26"},
    {"source": "Google Ads", "status": "Contacted", "title": "Sales Manager", "course": "CRM Automation", "created_date": "23-02-26"},
    {"source": "Organic Search", "status": "New", "title": "IT Consultant", "course": "Ethical Hacking", "created_date": "24-02-26"},
    {"source": "Referral", "status": "Converted", "title": "CTO", "course": "Executive Leadership", "created_date": "24-02-26"},
    {"source": "Webinar", "status": "Qualified", "title": "QA Engineer", "course": "Automated Testing", "created_date": "25-02-26"},
    {"source": "LinkedIn", "status": "New", "title": "UX Researcher", "course": "Design Thinking", "created_date": "25-02-26"},
    {"source": "Organic Search", "status": "Nurturing", "title": "Financial Analyst", "course": "Excel Macros & VBA", "created_date": "25-02-26"},
    {"source": "Facebook Ads", "status": "New", "title": "Small Business Owner", "course": "Social Media Marketing", "created_date": "26-02-26"},
    {"source": "Twitter", "status": "Unqualified", "title": "Accountant", "course": "Python for Finance", "created_date": "26-02-26"},
    {"source": "Google Ads", "status": "Contacted", "title": "Network Engineer", "course": "Cisco CCNA Prep", "created_date": "26-02-26"},
    {"source": "LinkedIn", "status": "New", "title": "Full Stack Dev", "course": "Node.js Microservices", "created_date": "27-02-26"},
    {"source": "Direct Traffic", "status": "Qualified", "title": "Graphic Designer", "course": "Motion Graphics", "created_date": "27-02-26"},
    {"source": "Referral", "status": "New", "title": "Graduate Student", "course": "Data Science Boot Camp", "created_date": "27-02-26"},
    {"source": "Webinar", "status": "Nurturing", "title": "SEO Specialist", "course": "Advanced SEO 2024", "created_date": "01-02-26"},
    {"source": "LinkedIn", "status": "Converted", "title": "Technical Writer", "course": "API Documentation", "created_date": "02-02-26"},
    {"source": "Organic Search", "status": "Contacted", "title": "Security Analyst", "course": "CompTIA Security+", "created_date": "03-02-26"},
    {"source": "Facebook Ads", "status": "New", "title": "E-commerce Manager", "course": "Shopify Mastery", "created_date": "04-02-26"},
    {"source": "Google Ads", "status": "Qualified", "title": "Database Admin", "course": "NoSQL Databases", "created_date": "05-02-26"},
    {"source": "Twitter", "status": "New", "title": "Copywriter", "course": "AI for Writing", "created_date": "06-02-26"},
    {"source": "LinkedIn", "status": "Nurturing", "title": "App Developer", "course": "SwiftUI & iOS", "created_date": "07-02-26"},
    {"source": "Webinar", "status": "Unqualified", "title": "Teacher", "course": "EdTech Integration", "created_date": "08-02-26"},
    {"source": "Referral", "status": "Contacted", "title": "VP of Engineering", "course": "Scaling Tech Teams", "created_date": "09-02-26"},
    {"source": "Direct Traffic", "status": "New", "title": "Web Designer", "course": "Webflow Mastery", "created_date": "10-02-26"},
    {"source": "Organic Search", "status": "Qualified", "title": "Risk Analyst", "course": "Quantitative Finance", "created_date": "11-02-26"},
    {"source": "Facebook Ads", "status": "New", "title": "Artist", "course": "NFT & Crypto Art", "created_date": "12-02-26"},
    {"source": "LinkedIn", "status": "Converted", "title": "Cloud Architect", "course": "Google Cloud Professional", "created_date": "13-02-26"},
    {"source": "Google Ads", "status": "Nurturing", "title": "Marketing Director", "course": "Omnichannel Strategy", "created_date": "14-02-26"},
    {"source": "Webinar", "status": "New", "title": "Logistics Coordinator", "course": "Supply Chain Mgmt", "created_date": "15-02-26"},
    {"source": "Twitter", "status": "Contacted", "title": "Blogger", "course": "Affiliate Marketing", "created_date": "16-02-26"},
    {"source": "Referral", "status": "New", "title": "HR Specialist", "course": "Conflict Resolution", "created_date": "17-02-26"},
    {"source": "Direct Traffic", "status": "Qualified", "title": "Frontend Dev", "course": "Vue.js Framework", "created_date": "18-02-26"},
    {"source": "LinkedIn", "status": "Nurturing", "title": "DevOps Engineer", "course": "Kubernetes in Practice", "created_date": "19-02-26"},
    {"source": "Organic Search", "status": "Converted", "title": "Product Manager", "course": "Product Analytics", "created_date": "20-02-26"},
    {"source": "Facebook Ads", "status": "Unqualified", "title": "Chef", "course": "Culinary Management", "created_date": "21-02-26"},
    {"source": "Google Ads", "status": "New", "title": "Legal Assistant", "course": "Legal Tech & AI", "created_date": "22-02-26"}
]



# unique sources

unique_sources = {l.get("source") for l in leads}
print(unique_sources)

# count of leads per source

count_of_leads_per_source = [l.get("source") for l in leads]
countpp =  {c:count_of_leads_per_source.count(c) for c in count_of_leads_per_source}
print(countpp)

# Google Ads Conversion Rate

google_ads_converted = [l for l in leads if l.get("source") == "Google Ads" and l.get("status") == "Converted"]
total_leads = [l for l in leads]
print(len(google_ads_converted)/len(total_leads)*100)

# status summary

status_all = [l.get("status") for l in leads]
status_all_count = {l:status_all.count(l) for l in status_all}
print(status_all_count)

qualified = status_all_count.get("Unqualified")/sum(status_all_count.values())*100 
print(qualified)