import streamlit as st
import PyPDF2

def extract_text_from_pdf(uploaded_file):
    try:
        uploaded_file.seek(0)
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + " "
        return text
    except Exception as e:
        return ""

st.set_page_config(page_title="Smart Resume Analyzer & Career Advisor", page_icon="📄", layout="wide")

st.title("📄 Multi-Domain Smart Resume Analyzer & Career Advisor")
st.write("Upload any Resume (CS / Tech, Marketing, Management, HR, Finance) to get instant domain-specific recommendations & salary insights!")

uploaded_file = st.file_uploader("Upload your Resume (PDF format)", type=["pdf"])

if uploaded_file is not None:
    if st.button("Analyze Resume "):
        resume_text = extract_text_from_pdf(uploaded_file)
        
        if not resume_text.strip():
            st.error("Error: Could not extract text from this PDF. Please try a different PDF resume.")
        else:
            st.success("Resume Analysis Successful!")
            text_lower = resume_text.lower()
            
            # --- KEYWORD COUNT SCORE FOR MULTI-DOMAIN CLASSIFICATION ---
            cs_keywords = ["python", "c++", "java", "c", "html", "css", "javascript", "developer", "software", "github", "data structures", "sql", "coding", "react", "node", "web"]
            marketing_keywords = ["marketing", "seo", "social media", "brand", "canva", "digital marketing", "campaign", "sales", "content", "bba", "mba", "lead generation", "copywriting"]
            hr_keywords = ["hr", "human resource", "recruitment", "hiring", "payroll", "employee", "interviews", "talent acquisition"]
            finance_keywords = ["finance", "accounting", "tally", "excel", "taxation", "banking", "financial", "audit", "gst"]

            score_cs = sum(1 for kw in cs_keywords if kw in text_lower)
            score_marketing = sum(1 for kw in marketing_keywords if kw in text_lower)
            score_hr = sum(1 for kw in hr_keywords if kw in text_lower)
            score_finance = sum(1 for kw in finance_keywords if kw in text_lower)

            # Determine Best Domain Match
            scores = {
                "CS": score_cs,
                "Marketing": score_marketing,
                "HR": score_hr,
                "Finance": score_finance
            }
            
            detected_domain = max(scores, key=scores.get)
            if scores[detected_domain] == 0:
                detected_domain = "General"

            st.markdown(f"###  Identified Domain: **{detected_domain} Profile**")
            
            st.markdown("---")
            st.markdown("###  Domain Specific Feedback & Improvement Ideas:")

            # --- 1. COMPUTER SCIENCE / TECH DOMAIN ---
            if detected_domain == "CS":
                st.markdown("""
                * **Resume Structure:** Clear technical profile detected with coding keywords.
                * **Key Enhancements:** 
                  1. Add active **GitHub repository links** for all your major projects.
                  2. List technical skills at the top sorted by (Languages, Frameworks, Developer Tools).
                """)
                
                st.markdown("###  Recommended Job Roles & Application Posts:")
                st.markdown("""
                1. **Software Developer Intern / Python Developer**  
                   * *Platforms:* Internshala, Wellfound, LinkedIn  
                   * *Fit:* Direct fit for programming, logic building, and backend support.
                2. **Junior Web Developer / Front-End Associate**  
                   * *Platforms:* LinkedIn, Instahyre  
                   * *Fit:* Good for building interactive UIs and web applications.
                3. **Associate Technical Engineering Trainee**  
                   * *Platforms:* Naukri.com, TCS/Infosys/Wipro hiring drives  
                   * *Fit:* Standard entry-level role for IT and software services.
                """)
                
                st.markdown("###  Estimated Entry-Level Salary Range:")
                st.info(" **Expected Package:** ₹3.5 LPA – ₹7.0 LPA (Depending on startup vs. product MNC / coding skills)")

            # --- 2. MARKETING & MANAGEMENT DOMAIN ---
            elif detected_domain == "Marketing":
                st.markdown("""
                * **Resume Structure:** Strong alignment with marketing, branding, and promotional activities.
                * **Key Enhancements:** 
                  1. Add links to your social media campaigns, portfolio, or Canva designs.
                  2. Focus on metrics (e.g., 'Grew reach by 30%', 'Managed 5 successful events').
                """)
                
                st.markdown("###  Recommended Job Roles & Application Posts:")
                st.markdown("""
                1. **Digital Marketing / Social Media Specialist**  
                   * *Platforms:* Internshala, LinkedIn, Wellfound  
                   * *Fit:* Focuses on social media management, brand strategy, and content creation.
                2. **Brand Management / Growth Marketing Trainee**  
                   * *Platforms:* LinkedIn, Naukri.com  
                   * *Fit:* Good for market analysis, user acquisition, and campaign strategy.
                3. **Business Development / Sales Associate**  
                   * *Platforms:* Wellfound (Startups), Internshala  
                   * *Fit:* Ideal for client management, lead generation, and business growth.
                """)
                
                st.markdown("### 💰 Estimated Entry-Level Salary Range:")
                st.info("📊 **Expected Package:** ₹3.0 LPA – ₹6.0 LPA (Plus performance incentives in sales/marketing roles)")

            # --- 3. HR DOMAIN ---
            elif detected_domain == "HR":
                st.markdown("""
                * **Resume Structure:** Human Resources and recruitment profile detected.
                * **Key Enhancements:** Mention communication skills, conflict resolution, and familiarity with HRMS or recruitment portals like LinkedIn Recruiter.
                """)
                
                st.markdown("###  Recommended Job Roles & Application Posts:")
                st.markdown("""
                1. **Talent Acquisition / HR Intern**  
                   * *Platforms:* Internshala, LinkedIn  
                   * *Fit:* Focuses on sourcing candidates, interviewing, and onboardings.
                2. **Employee Engagement Trainee**  
                   * *Platforms:* Naukri.com, LinkedIn  
                   * *Fit:* Great for organizational culture management and internal operations.
                """)
                
                st.markdown("### 💰 Estimated Entry-Level Salary Range:")
                st.info("📊 **Expected Package:** ₹2.8 LPA – ₹5.0 LPA (Standard corporate fresher range)")

            # --- 4. FINANCE & ACCOUNTS DOMAIN ---
            elif detected_domain == "Finance":
                st.markdown("""
                * **Resume Structure:** Finance and accounting background detected.
                * **Key Enhancements:** Highlight advanced MS Excel (VLOOKUP, Pivot tables), Tally, or GST/Taxation basic knowledge.
                """)
                
                st.markdown("### 💼 Recommended Job Roles & Application Posts:")
                st.markdown("""
                1. **Financial Analyst Trainee / Accounts Associate**  
                   * *Platforms:* LinkedIn, Naukri.com  
                   * *Fit:* Ideal for handling account reconciliations, financial reports, and auditing.
                2. **Taxation & Compliance Analyst**  
                   * *Platforms:* LinkedIn, Corporate Portals  
                   * *Fit:* Great fit for tax calculation and compliance operations.
                """)
                
                st.markdown("###  Estimated Entry-Level Salary Range:")
                st.info(" **Expected Package:** ₹3.0 LPA – ₹5.5 LPA (Depending on Excel/Tally expertise)")

            # --- 5. GENERAL / OTHER DOMAIN ---
            else:
                st.markdown("""
                * **Resume Structure:** General executive profile detected.
                * **Key Enhancements:** Add domain-specific keywords (Tech, Marketing, HR, or Finance) to increase visibility.
                """)
                
                st.markdown("###  Recommended Job Roles & Application Posts:")
                st.markdown("""
                1. **Operations / Business Support Analyst**  
                   * *Platforms:* Internshala, LinkedIn  
                   * *Fit:* Great multi-purpose entry-level corporate role.
                2. **Customer Success / Account Management Associate**  
                   * *Platforms:* Naukri, LinkedIn  
                   * *Fit:* Ideal for client relations and process management.
                """)
                
                st.markdown("### Estimated Entry-Level Salary Range:")
                st.info(" **Expected Package:** ₹2.5 LPA – ₹4.5 LPA")

            st.markdown("---")
            st.markdown("###  Top Job Platforms & Action Plan:")
            st.markdown("""
            * **Startups & High Growth Roles:** Wellfound (formerly AngelList), Instahyre
            * **Internships & Freshers:** Internshala, Unstop
            * **Corporate Positions:** LinkedIn, Naukri.com
            * **Next Step:** Directly message hiring managers or recruiters on LinkedIn with a customized introductory note alongside your resume!
            """)

else:
    st.info(" Please upload a PDF resume above to get an instant domain-based career audit.")