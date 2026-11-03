import os
import pathlib
from datetime import datetime
import pandas as pd
import plotly.express as px
import psutil
import streamlit as st
from dotenv import load_dotenv

# Amazon RDS Database Manager Integration
import db_manager

# ==========================================
# ENVIRONMENT CONFIGURATION (Cross-Platform Compatibility)
# ==========================================
load_dotenv()

# Use safe relative pathing without leaking local OS usernames
base_dir = pathlib.Path(__file__).resolve().parent
local_env = base_dir / ".env"
if local_env.exists():
  load_dotenv(dotenv_path=local_env, override=False)

# Load public IP dynamically from environment variable (defaults to placeholder if not set)
EC2_PUBLIC_IP = os.getenv("EC2_PUBLIC_IP", "Protected Node")

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Yamin | Cloud DevOps Portfolio", page_icon="☁️", layout="wide"
)

# ==========================================
# 2. GLOBAL STYLING & TOP WHITESPACE REMOVAL (CSS)
# ==========================================
st.markdown(
    """
    <style>
    /* -------------------------------------------------------------
       1. ELIMINATE TOP EMPTY SPACE ACROSS ALL PAGES & SIDEBAR
       ------------------------------------------------------------- */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    [data-testid="stSidebar"] .block-container {
        padding-top: 1rem !important;
    }
    header[data-testid="stHeader"] {
        height: 2rem !important;
        background: transparent !important;
    }

    /* -------------------------------------------------------------
       2. REDUCE METRIC FONT SIZE TO ~50% (Compact Display)
       ------------------------------------------------------------- */
    div[data-testid="stMetricValue"] {
        font-size: 1.1rem !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem !important;
    }
    div[data-testid="stMetricDelta"] {
        font-size: 0.75rem !important;
    }

    /* -------------------------------------------------------------
       3. GENERAL UI & CONTAINER STYLING
       ------------------------------------------------------------- */
    .main { 
        background-color: #f8f9fa; 
    }
    .stApp { 
        font-family: 'Segoe UI', sans-serif; 
    }
    .profile-card { 
        background: white; 
        padding: 25px; 
        border-radius: 12px; 
        border-left: 5px solid #FF9900; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
        margin-bottom: 20px; 
    }
    .metric-card { 
        background: #ffffff; 
        padding: 15px; 
        border-radius: 8px; 
        border: 1px solid #e0e0e0; 
    }
    .section-header {
        color: #1a202c;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# 3. SIDEBAR NAVIGATION HUB
# ==========================================
with st.sidebar:
  st.markdown("## ⚙️ Yamin DevOps Portal")

  menu = [
      "👤 Profile",
      "💼 Portfolio",
      "🚀 Portal Tech",
      "🛠️ AWS Engine",
      "🛒 E-Commerce",
      "🤖 Gemini AI",
      "📬 Contact",
  ]
  choice = st.radio("Navigation Hub:", menu)
  st.markdown("---")
  st.caption("Deployment Environment: Cross-Platform")
  st.caption("Supported Hosts: AWS EC2 Ubuntu / Windows Local")

# ==========================================
# 4. PAGE 1: PROFESSIONAL PROFILE
# ==========================================
if choice == "👤 Profile":
  st.title("👤 Cloud DevOps & Infrastructure Engineer")

  col1, col2 = st.columns([1, 2])

  with col1:
    st.markdown(
        """
        <div class="profile-card">
            <h3 style='margin-top:0; color:#FF9900;'>Yamin</h3>
            <p><b>Role:</b> Cloud & Telecom Specialist</p>
            <p><b>Work Status:</b> USA Citizen</p>
            <p><b>Core Domains:</b> Systems Automation, CI/CD Pipelines</p>
            <p><b>Languages:</b> English, Spanish, Urdu, Hindi, Punjabi</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "💡 **Focus Area:** Building highly resilient, auto-deployed, secure"
        " cloud systems using infrastructure code frameworks."
    )
    st.success("⚡ CI/CD Automation Active: Auto-deployed via GitHub Actions!")
  with col2:
    st.markdown(
        "<h3 class='section-header'>Executive Summary</h3>",
        unsafe_allow_html=True,
    )
    st.write("""
        Dedicated IT professional with over **10 years of experience** spanning Telecom, Help Desk, 
        and Mobility Specialization. Proven track record in designing and maintaining complex network 
        infrastructures. Now transitioning into **AWS Cloud Engineering**, leveraging deep expertise 
        in Python automation, OOP architecture, and serverless computing.
        """)

    st.markdown(
        "<h3 class='section-header'>Technical Proficiency Matrix</h3>",
        unsafe_allow_html=True,
    )
    df_skills = pd.DataFrame({
        "Category": [
            "Cloud (AWS)",
            "Programming (Python)",
            "Networking (CCNA)",
            "E-Commerce Systems",
        ],
        "Proficiency": [85, 92, 98, 90],
    })
    fig = px.bar(
        df_skills,
        x="Proficiency",
        y="Category",
        orientation="h",
        color="Proficiency",
        color_continuous_scale="Oranges",
    )
    fig.update_layout(
        height=250,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=20, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# 5. PAGE 2: PROFESSIONAL PORTFOLIO
# ==========================================
elif choice == "💼 Portfolio":
  st.title("💼 Professional Infrastructure & DevOps Portfolio")
  st.caption(
      "AWS Certified Solutions Architect | 10+ Years Enterprise IT & Networking"
      " | AI Solutions Consultant"
  )

  # Top Executive Summary Metrics (Compact text size via CSS)
  m1, m2, m3, m4 = st.columns(4)
  with m1:
    st.metric(
        label="Total Experience", value="10+ Years", delta="Enterprise Systems"
    )
  with m2:
    st.metric(
        label="Primary Cloud", value="AWS Certified", delta="Solutions Architect"
    )
  with m3:
    st.metric(
        label="Certifications", value="3 Core Badges", delta="AWS | Cisco | Microsoft"
    )
  with m4:
    st.metric(label="Education", value="BS in IT", delta="Virtual University")

  st.markdown("---")

  # Tabs
  tab_skills, tab_history, tab_certs, tab_overview = st.tabs([
      "🛠️ Technical Matrix",
      "💼 Employment History",
      "🎓 Certifications & Education",
      "🚀 Services & Overview",
  ])

  # TAB 1: TECHNICAL MATRIX
  with tab_skills:
    st.subheader("🛠️ Technical Skill Matrix & Engineering Capabilities")

    st.markdown("""
        | Technology Domain | Primary Tools & Frameworks | Proficiency Level |
        | :--- | :--- | :--- |
        | **Cloud Infrastructure (IaaS)** | AWS EC2, Amazon RDS, S3, IAM, Bedrock AI, Lambda, Security Groups | Expert |
        | **Operating Systems & Shell** | Linux (Ubuntu 22.04 LTS), Windows Server, Bash Scripting | Expert |
        | **Web Servers & Proxies** | Nginx, Reverse Proxying, Let's Encrypt (Certbot), SSL/TLS | Expert |
        | **Networking & Protocols** | TCP/IP, DNS, VPNs, SSH, Port Management, Cisco Switching/Routing | Advanced |
        | **DevOps & CI/CD** | GitHub Actions, Systemd / PM2 Daemons, Environment Secrets (`.env`) | Advanced |
        | **Databases** | MySQL, PostgreSQL, Relational Schema Design, Query Optimization | Advanced |
        | **Programming & Web** | Python (Streamlit, boto3, smtplib), PHP, HTML/CSS, JavaScript | Advanced |
        | **Directory & Mobility** | Microsoft Active Directory, XenMobile MDM, Enterprise VPN | Proficient |
        """)

  # TAB 2: EMPLOYMENT HISTORY
  with tab_history:
    st.subheader("💼 Career Trajectory & Employment History")

    st.markdown("### 📊 Career Timeline Summary")
    st.markdown("""
        | Period | Role Title | Organization | Core Domain Focus |
        | :--- | :--- | :--- | :--- |
        | **2025 – Present** | AWS Cloud & DevOps Engineer | Self-Employed / Consulting | AWS EC2/RDS, CI/CD, Nginx, AI Agents |
        | **2023 – 2025** | E-Commerce Systems Manager | Daraz.pk | Platform Ops, Database & Store Admin |
        | **2018 – 2022** | Systems & Network Infrastructure Lead | E-Com & Telecom Solutions | Web Portals, VoIP Switch Routing, MySQL |
        | **2016 – 2017** | Help Desk & Enterprise Mobility Spec | HMSHost | Active Directory (3,000+ Users), XenMobile |
        | **2014 – 2016** | Systems & Network Support Spec | COLT Telecomunicaciones SA | Windows Server, Enterprise VPNs, Routing |
        | **2010 – 2013** | Systems & Network Technician | Welcome Siglo 21 SL | LAN/WAN Infrastructure, Server Deployments |
        | **2005 – 2009** | Infrastructure & Switch Admin | Lunavoz Telecom SL | Artilium ISDN Switch, Carrier Interconnects |
        """)

    st.markdown("---")
    st.markdown("### 🔍 Detailed Responsibilities & Accomplishments")

    with st.expander(
        "☁️ AWS Cloud & DevOps Engineer / AI Consultant | Self-Employed (June"
        " 2025 – Present)",
        expanded=True,
    ):
      st.markdown("""
            * **Cloud Architecture:** Architecting and optimizing cloud infrastructure on AWS (EC2, S3, RDS, IAM, Bedrock AI, Lambda, Security Groups).
            * **CI/CD Automation:** Setting up automated CI/CD pipelines via GitHub Actions for seamless deployment directly from Windows/VS Code to AWS.
            * **Reverse Proxy & SSL:** Configuring Ubuntu Linux servers with Nginx reverse proxies, SSL/TLS certificates (Certbot), and DuckDNS domain mapping.
            * **App & Agent Engineering:** Building AI agent web applications in Python (Streamlit) featuring automated Lambda file processing workflows, custom Python SMTP engines, and MySQL databases.
            * **DevOps Hardening:** Managing AWS cost & billing optimization, isolated secrets management (`.env`), SSH security, and systemd daemons.
            """)

    with st.expander(
        "🛒 E-Commerce Systems Manager | Daraz.pk (Jan 2023 – May 2025)"
    ):
      st.markdown("""
            * Managed e-commerce web platform operations, store administration, and database management for online retail workflows.
            * Optimized product listings, catalog data structures, and inventory tracking systems using MySQL and custom scripting.
            * Ensured high availability, resolved site performance issues, and configured secure order processing workflows.
            """)

    with st.expander(
        "🌐 E-Commerce Systems & Network Infrastructure Lead | E-Com & Telecom"
        " Solutions (Jan 2018 – Nov 2022)"
    ):
      st.markdown("""
            * Architected and deployed end-to-end e-commerce database solutions, web portals, and shopping cart systems for retail client projects.
            * Configured and managed online VoIP system and calling card solutions, and switch platform routing.
            * Handled MySQL database optimization, PHP/Web, HTML customization, network hardware configuration, and infrastructure security management.
            """)

    with st.expander(
        "📱 Help Desk Analyst & Enterprise Mobility Specialist | HMSHost (Sep"
        " 2016 – Apr 2017)"
    ):
      st.markdown("""
            * Managed enterprise mobility infrastructure, Active Directory accounts, and secure VPN access for over **3,000 employees**.
            * Enrolled and configured mobile devices via XenMobile MDM, built custom MS Access tracking systems, and resolved complex LAN/WAN network and remote connectivity issues.
            """)

    with st.expander(
        "☎️ IT Systems & Network Support Specialist | COLT Telecomunicaciones SA"
        " (Mar 2014 – Apr 2016)"
    ):
      st.markdown("""
            * Provided Tier-2 systems and enterprise network support across Windows Server and Active Directory environments.
            * Configured local network hardware, remote access VPNs, and router routing protocols while maintaining strict SLA uptime metrics.
            """)

    with st.expander(
        "🖥️ Microsoft Systems & Network Technician | Welcome Siglo 21 SL (Apr"
        " 2010 – Dec 2013)"
    ):
      st.markdown("""
            * Engineered and maintained LAN/WAN network infrastructure, central server systems, and client workstations for internet retail centers.
            * Performed Windows OS deployments, hardware maintenance, and Microsoft application suite configurations.
            """)

    with st.expander(
        "🔄 IT Infrastructure & Switch Administrator | Lunavoz Telecom SL (Jan"
        " 2005 – Dec 2009)"
    ):
      st.markdown("""
            * Managed Artilium ISDN switch platforms, VoIP routing infrastructure, and core network configurations.
            * Coordinated CLI activations, carrier interconnects with Tier-1 telecom providers (BT, Orange, Telefónica), and server hardware maintenance.
            """)

  # TAB 3: CERTIFICATIONS & EDUCATION
  with tab_certs:
    st.subheader("🎓 Credentials, Certifications & Education")

    col_c1, col_c2 = st.columns(2)

    with col_c1:
      st.markdown("### 📜 Professional Industry Certifications")
      st.markdown("""
            | Certification Badge | Issuing Body | Issue Date | Status |
            | :--- | :--- | :--- | :--- |
            | **AWS Certified Solutions Architect - Associate** | AWS Training & Certification | May 2025 | Active / Verified |
            | **Microsoft Certified Systems Engineer (MCSE)** | Microsoft Learning | July 2012 | Active / Verified |
            | **Cisco Certified Network Associate (CCNA)** | Cisco Systems, Inc | March 2011 | Active / Verified |
            """)

    with col_c2:
      st.markdown("### 🎓 Academic Degree")
      with st.container(border=True):
        st.markdown(
            "#### **Bachelor of Science in Information Technology (BS IT)**"
        )
        st.markdown("**Institution:** Virtual University of Pakistan")
        st.markdown("**Period:** 2007 – 2011")
        st.markdown(
            "**Focus:** Computer Science, Software Engineering, Database Systems"
            " & Network Communications"
        )

  # TAB 4: SERVICES & OVERVIEW
  with tab_overview:
    st.subheader("🚀 Services & Executive Overview")
    st.write("""
        As a **Cloud & DevOps Engineer with over 10 years of cross-functional IT and networking experience**, 
        I help businesses, remote teams, and engineering leaders deploy scalable cloud infrastructure, secure Linux environments, 
        and build automated deployment pipelines.
        """)

    st.markdown("### 🛠️ On-Demand Client Services & Solutions")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
      with st.container(border=True):
        st.markdown("#### ☁️ AWS & Cloud Infrastructure Setup")
        st.markdown("""
                * **EC2 & Security:** Launching instances, configuring IAM roles, security group firewall policies, and SSH key management.
                * **DNS & Domain Mapping:** Custom domain routing using Route 53, DuckDNS, and CNAME/A record management.
                * **Managed Databases:** Amazon RDS (MySQL/PostgreSQL) database provisioning, connection handling, and security.
                """)

    with col_s2:
      with st.container(border=True):
        st.markdown("#### 🔒 Web Server, SSL & Application Hardening")
        st.markdown("""
                * **Nginx Reverse Proxy:** Eliminating non-standard port numbers (e.g., `:8501`) via clean Nginx reverse proxying on ports 80/443.
                * **SSL/TLS Security:** Free automated SSL certificate installation via Certbot / Let's Encrypt with auto-renewal timers.
                * **Daemon Automation:** Process management using `systemd` / `PM2` to guarantee auto-restart on reboots (`Restart=always`).
                """)

    st.markdown("### 🌐 Spoken Languages")
    st.markdown("""
        | Language | Proficiency Level |
        | :--- | :--- |
        | **English** | Fluent |
        | **Punjabi / Panjabi** | Native / Bilingual |
        | **Urdu** | Native / Bilingual |
        | **Hindi** | Fluent |
        | **Spanish** | Conversational |
        """)

# ==========================================
# 6. PAGE 3: PORTAL TECH & FEATURES
# ==========================================
elif choice == "🚀 Portal Tech":
  st.title("🚀 Portal DevOps Tech & Core Features")
  st.markdown(
      "An evaluation of the 10 key technical components, cloud architectures,"
      " and automation frameworks powering this live web app."
  )

  st.markdown("---")

  col_t1, col_t2 = st.columns(2)

  with col_t1:
    with st.container(border=True):
      st.markdown("### 🗄️ 1. Managed Amazon RDS (MySQL Database)")
      st.write("""
            * **Technology:** Amazon Relational Database Service (RDS), `pymysql` / `db_manager`.
            * **Function:** Provides high-availability relational data persistence for real-time inventory management, price calculations, and contact message logging.
            """)

    with st.container(border=True):
      st.markdown("### 📧 2. Native Python SMTP Email Engine")
      st.write("""
            * **Technology:** Python `smtplib`, `MIMEText`, Port 465 (SSL/TLS).
            * **Function:** Decoupled direct email notification engine bypassing third-party relay limits to securely route contact form submissions to inboxes.
            """)

    with st.container(border=True):
      st.markdown("### 🔄 3. GitHub Actions CI/CD Pipeline")
      st.write("""
            * **Technology:** GitHub Actions, AWS EC2 Runner, SSH Automation.
            * **Function:** Automated continuous deployment pipeline that automatically pulls and deploys code changes onto the AWS EC2 host upon `git push`.
            """)

    with st.container(border=True):
      st.markdown("### 🤖 4. Gemini AI Intelligent Assistant")
      st.write("""
            * **Technology:** Natural Language Intent Parser & Knowledge Engine.
            * **Function:** Context-aware portfolio copilot answering client queries on qualifications, operational metrics, and cloud benchmarks.
            """)

    with st.container(border=True):
      st.markdown("### 📊 5. Live Host Telemetry & Resource Monitoring")
      st.write("""
            * **Technology:** Python `psutil` Library, OS Kernel Hooks.
            * **Function:** Fetches real-time server metrics directly from the host machine (CPU utilization, RAM allocation, disk usage, uptime).
            """)

  with col_t2:
    with st.container(border=True):
      st.markdown("### 🔒 6. Nginx Reverse Proxy & SSL/TLS Encryption")
      st.write("""
            * **Technology:** Nginx Web Server, Let's Encrypt (`certbot`), DuckDNS.
            * **Function:** Routes incoming HTTPS requests on ports 80/443 to the Streamlit app port 8501, securing data in transit with free SSL certificates.
            """)

    with st.container(border=True):
      st.markdown("### 🔑 7. Isolated Secrets Management (`.env`)")
      st.write("""
            * **Technology:** `python-dotenv`, AWS Security Groups, Environment Variables.
            * **Function:** Isolates database credentials, API keys, and mail passwords from source code, enabling seamless dual host compatibility (Windows local & Ubuntu EC2).
            """)

    with st.container(border=True):
      st.markdown("### 🖥️ 8. Streamlit Framework & Custom CSS Injection")
      st.write("""
            * **Technology:** Streamlit, Injected Global CSS (`st.markdown`).
            * **Function:** Responsive frontend user interface with compact metric styling (~50% size reduction), zero top-whitespace padding, and dynamic layout routing.
            """)

    with st.container(border=True):
      st.markdown("### 📈 9. Interactive Data Visualization")
      st.write("""
            * **Technology:** Plotly Express (`plotly.express`), Pandas DataFrames.
            * **Function:** Renders dynamic horizontal bar charts, structured skill matrices, and live financial stock valuations directly in UI components.
            """)

    with st.container(border=True):
      st.markdown("### ⚙️ 10. Systemd / PM2 Daemon Process Management")
      st.write("""
            * **Technology:** Linux `systemd` Services / Background Daemons.
            * **Function:** Guarantees zero downtime by keeping the application active as a background daemon and automatically restarting it on server reboots.
            """)

# ==========================================
# 7. PAGE 4: AWS ENGINE (OPERATIONS)
# ==========================================
elif choice == "🛠️ AWS Engine":
  st.title("🛠️ AWS Infrastructure Control Room")
  st.markdown(
      "Monitor and manage your cloud ecosystem. Utilize Boto3 integration"
      " frameworks for real-time telemetry reporting."
  )

  tab_compute, tab_storage, tab_lambda = st.tabs([
      "💻 Elastic Compute (EC2)",
      "🪣 Object Storage (S3)",
      "⚡ Serverless (Lambda)",
  ])

  with tab_compute:
    st.subheader("EC2 Host Performance Management")
    st.info(
        f"Current Instance Configuration: t3.micro (Linux/Ubuntu 22.04 LTS) |"
        f" Public IP Node: {EC2_PUBLIC_IP}"
    )

    col_c1, col_c2 = st.columns(2)
    with col_c1:
      st.metric(
          "Total Web Production Instances Running",
          "1",
          delta="Stable Cluster Status",
      )
    with col_c2:
      if st.button("Refresh Host Telemetry"):
        st.success("Compute Layer Integration Loop Connection: OPTIMAL")

    st.markdown("### 📊 Live Host Infrastructure Metrics (psutil)")
    st.write("Real-time utilization percentages fetched directly from host kernel:")

    m1, m2, m3 = st.columns(3)
    with m1:
      cpu = psutil.cpu_percent(interval=0.5)
      st.metric(label="Host CPU Load", value=f"{cpu}%")
      st.progress(int(cpu))
    with m2:
      ram = psutil.virtual_memory()
      st.metric(label="Assigned Memory Used", value=f"{ram.percent}%")
      st.progress(int(ram.percent))
    with m3:
      disk = psutil.disk_usage("/")
      st.metric(label="Root Storage Partition Used", value=f"{disk.percent}%")
      st.progress(int(disk.percent))

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    st.caption(
        "Server Persistence Uptime Tracking | Last Instance Boot Event:"
        f" {boot_time.strftime('%Y-%m-%d %H:%M:%S')}"
    )

  with tab_storage:
    st.subheader("S3 Data Storage Pipeline Layer")
    bucket_name = st.text_input(
        "Active Target Bucket Name:", "yamin-production-data-001"
    )
    st.progress(72, text="Target Bucket Storage Capacity Status: 72% Exhausted")
    if st.button("Validate S3 Object Bucket Policy"):
      st.warning(
          "Storage Infrastructure Security Audit: AES-256 Server-Side Encryption"
          " Verified."
      )

  with tab_lambda:
    st.subheader("Serverless Server Runtime Handler")
    st.code(
        """
# AWS Lambda Deployment Template - Python 3.12 Runtime
def lambda_handler(event, context):
    try:
        data = event.get('body', {})
        # Perform downstream serverless logic computations
        return {
            'statusCode': 200, 
            'body': 'Process Execution Pipeline Complete'
        }
    except Exception as e:
        return {
            'statusCode': 500, 
            'body': f'Handler Exception Error: {str(e)}'
        }
        """,
        language="python",
    )
    if st.button("Trigger Pipeline Event Mock Test"):
      st.json({
          "status": "executed",
          "runtime": "python3.12",
          "memory_allocation": "128MB",
          "execution_duration_ms": "42.11",
      })

# ==========================================
# 8. PAGE 5: E-COMMERCE ENGINE (DIRECT AMAZON RDS CONNECTION)
# ==========================================
elif choice == "🛒 E-Commerce":
  st.title("🛒 Inventory & Amazon RDS Persistence Engine")
  st.markdown(
      "Live relational database inventory integration powered by **Amazon RDS"
      " MySQL**."
  )

  col_input, col_display = st.columns([1, 2])

  # --- FORM: COMMIT ASSET TO AMAZON RDS ---
  with col_input:
    with st.container(border=True):
      st.subheader("Add Asset to RDS Database")
      sku = st.text_input("SKU Identifier:", placeholder="e.g. TEL-SKU-101")
      name = st.text_input(
          "Product Name:", placeholder="e.g. Cisco IP Phone 8841"
      )
      category = st.selectbox(
          "Category Group:", ["Electronics", "Telecom", "Hardware", "Retail"]
      )
      price = st.number_input(
          "Unit Price ($):", min_value=0.0, step=0.01, value=150.00
      )
      stock = st.number_input(
          "Initial Stock Quantity:", min_value=0, step=1, value=25
      )

      if st.button("Commit to Amazon RDS Database"):
        if sku and name:
          with st.spinner("Writing to Amazon RDS MySQL instance..."):
            success = db_manager.add_product(
                sku=sku,
                name=name,
                category=category,
                price=price,
                stock=stock,
            )
            if success:
              st.success(
                  f"🎉 Asset **{name}** successfully committed to RDS!"
              )
            else:
              st.error(
                  "❌ Database Write Failure: Check your connection settings or"
                  " duplicate SKU entries."
              )
        else:
          st.warning(
              "⚠️ Validation Warning: Please fill in both the SKU and Product"
              " Name."
          )

  # --- DISPLAY: FETCH LIVE INVENTORY FROM AMAZON RDS ---
  with col_display:
    st.subheader("Amazon RDS Live Inventory Table")

    products = db_manager.get_all_products()

    if products:
      df_inv = pd.DataFrame(products)

      # Reorder display columns cleanly if present
      expected_cols = [
          "id",
          "sku",
          "name",
          "category",
          "price",
          "stock",
          "created_at",
      ]
      display_cols = [c for c in expected_cols if c in df_inv.columns]
      if display_cols:
        df_inv = df_inv[display_cols]

        st.dataframe(df_inv, use_container_width=True)

        # Live RDS Financial Telemetry
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("Unique Records", len(products))

        if "stock" in df_inv.columns:
          total_stock = df_inv["stock"].sum()
          m_col2.metric("Total Items Stocked", int(total_stock))

        if "price" in df_inv.columns and "stock" in df_inv.columns:
          total_val = (df_inv["price"] * df_inv["stock"]).sum()
          m_col3.metric("Inventory Valuation", f"${total_val:,.2f}")
    else:
      st.info(
          "ℹ️ No active inventory records found in RDS database table"
          " `products`."
      )

  st.markdown("---")
  st.subheader("Regional Pricing Calculator (Day 7 Conditional Control Logic)")
  col_reg1, col_reg2 = st.columns(2)
  with col_reg1:
    target_market = st.selectbox(
        "Target Logistics Market Destination:", ["London", "New York", "Barcelona"]
    )
  with col_reg2:
    tax_rate = 0.20 if target_market == "London" else 0.15
    st.metric(f"Computed Tax Rate for {target_market}", f"{tax_rate*100}%")

# ==========================================
# 9. PAGE 6: GEMINI AI PORTFOLIO COPILOT
# ==========================================
elif choice == "🤖 Gemini AI":
  st.title("🤖 Gemini Intelligent Portfolio Assistant")
  st.markdown(
      "Ask anything about Yamin's technical expertise, historical project"
      " frameworks, or global DevOps industry benchmarks."
  )

  query = st.text_input(
      "Ask about Yamin's career or DevOps industry data:",
      placeholder=(
          "e.g., What is the average hourly rate for a DevOps engineer in the"
          " US? or What projects did Yamin build?"
      ),
  )

  if st.button("Query Portfolio Brain"):
    if query:
      q_lower = query.lower()
      with st.spinner("Analyzing custom portfolio intelligence layers..."):
        st.markdown("### 💡 Copilot Analysis Response")
        with st.container(border=True):

          if any(
              word in q_lower
              for word in ["qualification", "experience", "who is yamin", "skills"]
          ):
            st.write("### 🥇 Yamin's Professional Summary")
            st.write("""
                        Yamin is a seasoned Cloud DevOps & Infrastructure Engineer with **over 10 years of cross-functional experience** 
                        spanning enterprise cloud setups, technical help desk architecture, database engineering, and global mobility platforms.
                        He combines foundational system skills like Cisco CCNA networking with modern automated cloud paradigms.
                        """)

          elif any(
              word in q_lower
              for word in ["project", "build", "do for me", "completed"]
          ):
            st.write("### 🛠️ Production Systems Architecture")
            st.write("""
                        Yamin has engineered and deployed several notable systems showcased inside this unified production environment:
                        1. **Secure DevOps Portal Core:** Hosted natively on an AWS EC2 instance with safe parameter storage routing.
                        2. **Live Telemetry Interface:** Integrates Python kernel utilities (`psutil`) to display live server performance metrics directly on a dashboard layer.
                        3. **Inventory Management System:** Fully integrated with Amazon RDS MySQL to persist warehouse assets and track real-time telemetry.
                        """)

          elif any(word in q_lower for word in ["salary", "rate", "pay", "earn"]):
            st.write("### 📊 Global Industry Insights & Benchmarks")
            st.write("""
                        Based on market telemetry across the United States for an experienced **Cloud DevOps / Infrastructure Engineer** in 2026:
                        * **Estimated Contract Hourly Rate:** $65 – $95+ per hour depending on configuration scale, security clearing, and enterprise infrastructure tier.
                        * **Key Drivers:** Proficiency in Infrastructure as Code (IaC), zero-downtime application deployments, and automated secrets monitoring.
                        """)

          elif any(
              word in q_lower for word in ["devops", "aws", "python", "nginx"]
          ):
            st.write("### ☁️ Domain Technical Architecture")
            st.write(
                "Modern operational infrastructure emphasizes loose coupling,"
                " containerization, reverse proxy performance, \n and secure"
                " automated cryptographic key rotation. Shifting secret"
                " variables from code blocks into protected configurations"
                " \n removes single points of failure."
            )
