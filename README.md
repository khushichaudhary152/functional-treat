<div align="center">

🐍📊 FUNCTIONAL-TREAT


<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/1D%20%7C%202D%20Data-00B894?style=for-the-badge">
  <img src="https://img.shields.io/badge/Recursion-E84393?style=for-the-badge">
  <img src="https://img.shields.io/badge/Lambda-FD9644?style=for-the-badge">
  <img src="https://img.shields.io/badge/Beginner%20Friendly-6C5CE7?style=for-the-badge">
</p>

💻 Learn • Analyze • Transform • Practice

</div>

⸻

📖 Overview

functional-treat is a beginner-friendly Python console application designed to practice different Python programming concepts through numerical data processing.

The program allows the user to enter both 1D and 2D data and perform different operations such as calculating data summaries, finding unique and duplicate values, calculating factorial using recursion, filtering data using lambda functions, sorting data, and displaying dataset statistics.

This project brings multiple Python concepts together into one interactive, menu-driven application.

# ✨ Features

This project combines multiple Python features in one interactive application.

```mermaid
flowchart LR

    A["✨ FEATURES"]

    B["🔢 1D DATA"]
    C["🧮 2D DATA"]
    D["📊 DATA SUMMARY"]
    E["🔍 DATA ANALYSIS"]

    F["♻️ RECURSION"]
    G["⚡ LAMBDA"]
    H["📈 SORTING"]
    I["📊 STATISTICS"]

    B1["User Input"]
    B2["Numerical Values"]

    C1["Rows and Columns"]
    C2["2D Display"]

    D1["Total Elements"]
    D2["Minimum and Maximum"]
    D3["Sum and Average"]

    E1["Unique Values"]
    E2["Duplicate Values"]

    F1["Factorial"]
    F2["Recursive Function"]

    G1["Threshold"]
    G2["Filter Function"]

    H1["Ascending"]
    H2["Descending"]

    I1["Minimum"]
    I2["Maximum"]
    I3["Sum"]
    I4["Average"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    A --> G
    A --> H
    A --> I

    B --> B1
    B --> B2

    C --> C1
    C --> C2

    D --> D1
    D --> D2
    D --> D3

    E --> E1
    E --> E2

    F --> F1
    F --> F2

    G --> G1
    G --> G2

    H --> H1
    H --> H2

    I --> I1
    I --> I2
    I --> I3
    I --> I4

    style A fill:#6C5CE7,stroke:#FFFFFF,stroke-width:4px,color:#FFFFFF

    style B fill:#00B894,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style C fill:#0984E3,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style D fill:#E84393,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style E fill:#FD9644,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style F fill:#A55EEA,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style G fill:#00CEC9,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style H fill:#2D98DA,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style I fill:#D63031,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF

    style B1 fill:#55EFC4,stroke:#00B894,color:#222222
    style B2 fill:#81ECEC,stroke:#00CEC9,color:#222222

    style C1 fill:#74B9FF,stroke:#0984E3,color:#222222
    style C2 fill:#A29BFE,stroke:#6C5CE7,color:#FFFFFF

    style D1 fill:#FF7675,stroke:#E84393,color:#FFFFFF
    style D2 fill:#FD79A8,stroke:#E84393,color:#FFFFFF
    style D3 fill:#FAB1A0,stroke:#E1701A,color:#222222

    style E1 fill:#FFEAA7,stroke:#FD9644,color:#222222
    style E2 fill:#FFCC80,stroke:#E1701A,color:#222222

    style F1 fill:#D6A2E4,stroke:#A55EEA,color:#222222
    style F2 fill:#C39BD3,stroke:#7B3FC6,color:#FFFFFF

    style G1 fill:#81ECEC,stroke:#00CEC9,color:#222222
    style G2 fill:#74B9FF,stroke:#0984E3,color:#222222

    style H1 fill:#A29BFE,stroke:#6C5CE7,color:#FFFFFF
    style H2 fill:#C8D6E5,stroke:#2D98DA,color:#222222

    style I1 fill:#FF7675,stroke:#D63031,color:#FFFFFF
    style I2 fill:#FD79A8,stroke:#E84393,color:#FFFFFF
    style I3 fill:#FAB1A0,stroke:#E1701A,color:#222222
    style I4 fill:#FFCC80,stroke:#FD9644,color:#222222
```

---

# 🔄 Program Flow

```mermaid
flowchart TD

    A(["🚀 START"])
    B["📋 DISPLAY MAIN MENU"]
    C{"🔢 ENTER CHOICE"}

    D["1️⃣ INPUT DATA"]
    E["2️⃣ DATA SUMMARY"]
    F["3️⃣ CALCULATE FACTORIAL"]
    G["4️⃣ FILTER DATA"]
    H["5️⃣ SORT DATA"]
    I["6️⃣ DISPLAY STATISTICS"]
    J(["7️⃣ EXIT PROGRAM"])

    K{"📊 SELECT DATA TYPE"}
    L["🔢 ENTER 1D DATA"]
    M["🧮 ENTER 2D DATA"]
    N["💾 STORE DATA"]

    O["📊 FIND SUMMARY"]
    P["✨ UNIQUE VALUES"]
    Q["🔁 DUPLICATE VALUES"]
    R["📤 DISPLAY SUMMARY"]

    S["♻️ RECURSIVE FACTORIAL"]
    T["📤 DISPLAY RESULT"]

    U["⚡ ENTER THRESHOLD"]
    V["🔍 APPLY FILTER"]
    W["📤 DISPLAY FILTERED DATA"]

    X{"↕️ SELECT SORTING"}
    Y["⬆️ ASCENDING"]
    Z["⬇️ DESCENDING"]
    AA["📤 DISPLAY SORTED DATA"]

    AB["📈 MINIMUM"]
    AC["📈 MAXIMUM"]
    AD["➕ SUM"]
    AE["📊 AVERAGE"]
    AF["📤 DISPLAY STATISTICS"]

    AG(["👋 GOODBYE"])

    A --> B
    B --> C

    C --> D
    C --> E
    C --> F
    C --> G
    C --> H
    C --> I
    C --> J

    D --> K
    K --> L
    K --> M
    L --> N
    M --> N
    N --> B

    E --> O
    O --> P
    P --> Q
    Q --> R
    R --> B

    F --> S
    S --> T
    T --> B

    G --> U
    U --> V
    V --> W
    W --> B

    H --> X
    X --> Y
    X --> Z
    Y --> AA
    Z --> AA
    AA --> B

    I --> AB
    I --> AC
    I --> AD
    I --> AE
    AB --> AF
    AC --> AF
    AD --> AF
    AE --> AF
    AF --> B

    J --> AG

    style A fill:#00B894,stroke:#FFFFFF,stroke-width:4px,color:#FFFFFF
    style B fill:#6C5CE7,stroke:#FFFFFF,stroke-width:4px,color:#FFFFFF
    style C fill:#FDCB6E,stroke:#FFFFFF,stroke-width:4px,color:#222222

    style D fill:#0984E3,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style E fill:#00CEC9,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style F fill:#E84393,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style G fill:#FD9644,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style H fill:#A55EEA,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style I fill:#2D98DA,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style J fill:#D63031,stroke:#FFFFFF,stroke-width:4px,color:#FFFFFF

    style K fill:#FDCB6E,stroke:#E0A800,stroke-width:3px,color:#222222
    style X fill:#FDCB6E,stroke:#E0A800,stroke-width:3px,color:#222222

    style N fill:#20BF6B,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style R fill:#20BF6B,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style T fill:#20BF6B,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style W fill:#20BF6B,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style AA fill:#20BF6B,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF
    style AF fill:#20BF6B,stroke:#FFFFFF,stroke-width:2px,color:#FFFFFF

    style AG fill:#D63031,stroke:#FFFFFF,stroke-width:4px,color:#FFFFFF
```
## 📋 Main Menu Flowchart

```mermaid
flowchart TD
    A[START] --> B[MAIN MENU]
    B --> C{ENTER CHOICE}

    C --> D[1. INPUT DATA]
    C --> E[2. DATA SUMMARY]
    C --> F[3. CALCULATE FACTORIAL]
    C --> G[4. FILTER DATA]
    C --> H[5. SORT DATA]
    C --> I[6. DISPLAY STATISTICS]
    C --> J[7. EXIT PROGRAM]

    D --> B
    E --> B
    F --> B
    G --> B
    H --> B
    I --> B

    J --> K[GOODBYE]

    style A fill:#00B894,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#6C5CE7,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#FDCB6E,stroke:#333,stroke-width:2px,color:#000

    style D fill:#0984E3,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#00CEC9,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#E84393,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#FD9644,stroke:#333,stroke-width:2px,color:#fff
    style H fill:#A55EEA,stroke:#333,stroke-width:2px,color:#fff
    style I fill:#2D98DA,stroke:#333,stroke-width:2px,color:#fff
    style J fill:#D63031,stroke:#333,stroke-width:2px,color:#fff
    style K fill:#D63031,stroke:#333,stroke-width:2px,color:#fff
```

## 🖥️ Sample Output — 1D Array

```mermaid
flowchart TD

    A([🚀 PROGRAM START]) --> B[📋 MAIN MENU]
    B --> C[1. INPUT DATA]

    C --> D[🔢 SELECT 1D ARRAY]
    D --> E["Input: 23 36 48 59 62 75 83 91"]
    E --> F[✅ Data Stored Successfully]

    F --> G[📊 DATA SUMMARY]
    G --> G1["Total Elements: 8"]
    G --> G2["Minimum: 23"]
    G --> G3["Maximum: 91"]
    G --> G4["Sum: 477"]
    G --> G5["Average: 59.62"]
    G --> G6["Unique: 23, 36, 48, 59, 62, 75, 83, 91"]
    G --> G7["Duplicates: []"]

    G7 --> H[♻️ CALCULATE FACTORIAL]
    H --> H1["Input: 6"]
    H1 --> H2["Factorial of 6 = 720"]

    H2 --> I[🔍 FILTER DATA]
    I --> I1["Threshold: 50"]
    I1 --> I2["Filtered: 59, 62, 75, 83, 91"]

    I2 --> J[↕️ SORT DATA]
    J --> J1["Ascending: 23, 36, 48, 59, 62, 75, 83, 91"]
    J --> J2["Descending: 91, 83, 75, 62, 59, 48, 36, 23"]

    J2 --> K[📈 DATASET STATISTICS]
    K --> K1["Minimum: 23"]
    K --> K2["Maximum: 91"]
    K --> K3["Sum: 477"]
    K --> K4["Average: 59.62"]

    K4 --> L([👋 EXIT — Choice 7])

    style A fill:#00B894,stroke:#333,stroke-width:3px,color:#fff
    style B fill:#6C5CE7,stroke:#333,stroke-width:3px,color:#fff
    style C fill:#0984E3,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#74B9FF,stroke:#333,stroke-width:2px,color:#222
    style E fill:#55EFC4,stroke:#333,stroke-width:2px,color:#222
    style F fill:#20BF6B,stroke:#333,stroke-width:2px,color:#fff

    style G fill:#00CEC9,stroke:#333,stroke-width:2px,color:#fff
    style H fill:#E84393,stroke:#333,stroke-width:2px,color:#fff
    style I fill:#FD9644,stroke:#333,stroke-width:2px,color:#fff
    style J fill:#A55EEA,stroke:#333,stroke-width:2px,color:#fff
    style K fill:#2D98DA,stroke:#333,stroke-width:2px,color:#fff

    style L fill:#D63031,stroke:#333,stroke-width:3px,color:#fff
```

## 🧩 Concepts & Their Purpose

| 🔹 Concept | 🎯 Purpose |
|---|---|
| 📦 **1D & 2D Data** | Store and manage user-entered data |
| 🧮 **Built-in Functions** | Calculate minimum, maximum, sum and average |
| 🔁 **Recursion** | Calculate the factorial of a number |
| ⚡ **Lambda Function** | Apply conditions for filtering data |
| 🔍 **filter()** | Filter values based on a threshold |
| ↕️ **Sorting** | Arrange data in ascending or descending order |
| 📊 **Multiple Return Values** | Return multiple statistical values together |
| 🌐 **Global Variables** | Store dataset statistics globally |
| 🧩 **\*args & \*\*kwargs** | Handle variable numbers of arguments |
| 🔄 **Loops & Conditions** | Control menu operations and data processing |

 <div align="center">

# 📸 SCREENSHOTS

### 🖥️ Project Output

 (<img width="1920" height="8513" alt="op ss" src="https://github.com/user-attachments/assets/34a3423e-7706-4779-86a4-7eb20ffb87f0" />)

</div>

---

<div align="center">

# 🎥 DEMO VIDEO


(https://github.com/user-attachments/assets/67b9a6ea-529b-4cf1-85b3-ca442c03661b)

</div>

---

<div align="center">

# ✨ PROJECT HIGHLIGHTS

</div>

| 🚀 Feature | 💡 Description |
|:---:|---|
| 📦 **1D & 2D Data** | Handles both one-dimensional and two-dimensional data |
| 📊 **Data Summary** | Calculates total, minimum, maximum, sum and average |
| 🔁 **Recursion** | Calculates factorial using recursive logic |
| ⚡ **Lambda + filter()** | Filters data based on a threshold |
| ↕️ **Sorting** | Supports ascending and descending order |
| 🧩 **\*args & \*\*kwargs** | Demonstrates flexible function arguments |
| 🌐 **Global Variables** | Maintains dataset statistics |
| 🔄 **Menu Driven** | Simple and interactive console-based program |

---

<div align="center">

# 👩‍💻 AUTHOR

### **Khushi Chaudhary**

🐍 Python Developer & Computer Engineering Student

<br>

**Project:** `functional-treat`

</div>

---

<div align="center">

# 🙏 THANK YOU

### 💙 Thank you for visiting my project!

⭐ **If you like this project, consider giving it a star!**

<br>

**Keep Learning • Keep Coding • Keep Growing 🚀**

</div>



