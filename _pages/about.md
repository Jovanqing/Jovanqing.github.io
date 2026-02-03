---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@main/" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/main/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# 👤 About Me

Hi! I’m Yongqing Jiang, a joint PhD student at **Sichuan University (SCU)** and **Nanyang Technological University (NTU)**, under the supervision of <a href="https://acem.scu.edu.cn/info/1282/10761.htm" target="_blank">**Prof. Kaoshan Dai**</a> and Prof <a href="https://dr.ntu.edu.sg/entities/person/Shen-Zhiqi">**Prof. Zhiqi Shen**</a>.
My research resides at the intersection of **_Civil Engineering_** and **_Computer Science_**.
Prior to my doctoral studies at SCU, I gained significant research experience at the <a href="https://www-443.webvpn.sdjzu.edu.cn/xdxy/szdsys/sysjj.htm" target="_blank">**Shandong Key Laboratory of Intelligent Building Technology**</a>.

My research interest focuses on applying artificial intelligence and deep learning to intelligent 
infrastructure systems, which can be divided as follows:
- Structural Health Monitoring (SHM).
- AI and Data Science in Engineering.
- Large Language Models (LLMs) & Vision-Language Models (VLMs).
- Intelligent and Resilient Infrastructures.

Email: <a href="https://www-443.webvpn.sdjzu.edu.cn/xdxy/szdsys/sysjj.htm" target="_blank">yongqingjiang97@gmail.com</a>

My publications and citation statistics are available on 
<a href="https://scholar.google.com/citations?hl=zh-CN&user=WmV_Z7UAAAAJ">
Google Scholar
</a>
&nbsp;
<img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations&cacheSeconds=0&v=451">

Note: I am currently open to academic opportunities. Please feel free to contact me regarding any available positions.

# 🔥 News
- *2026.01*: &nbsp;🎉🎉 Our paper "Large language model for post-earthquake structural damage assessment of buildings" has been selected as the <strong>Featured Cover</strong> of <em>Computer-Aided Civil and Infrastructure Engineering</em>, recommended by Editor-in-Chief <a href="https://scholar.google.com/citations?user=TQMpoh8AAAAJ&hl=zh-CN" target="_blank"><strong>Prof. Hojjat Adeli</strong></a>. 
- *2025.12*: &nbsp;🎉🎉 Honored to lead our team to win the <strong>National Second Prize</strong> in the <a href="https://cpipc.acge.org.cn/cw/hp/2c90801795a92a850195d03b537b1bac" target="_blank"><strong>2025 First China Graduate Intelligent Construction Innovation Competition</strong></a>. 

# 📝 Selective Publications
<div class="paper-box">
  <div class="paper-box-image">
    <div>
      <div class="badge">Automation in Construction 2026</div>
      <img src="/images/AIC.GIF" alt="Post-earthquake structural damage assessment" width="100%">
    </div>
  </div>

  <div class="paper-box-text">

    <p>
      <a href="https://doi.org/10.1016/j.autcon.2025.106720">
        Multitask Unified Large Vision-Language Model for Post-Earthquake Structural Damage Assessment of Buildings
      </a>
    </p>

    <p>
      <strong>Yongqing Jiang</strong>, Jianze Wang, Xinyi Shen,a, Kaoshan Dai, Qingzi Ge
    </p>

    <p>
      <a href="https://doi.org/10.1016/j.autcon.2025.106720"><strong>Project</strong></a>
    </p>

    <ul>
      <li>
        We develop a multitask unified vision-language model for post-earthquake structural damage assessment,
        supported by instruction-based multi-task learning, a two-stage assessment framework,
        and a large-scale multi-attribute image–text dataset.
      </li>
    </ul>

  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image">
    <div>
      <div class="badge">Computer-Aided Civil and Infrastructure Engineering 2025</div>
      <div class="badge" style="background-color: #f39c12; top: 32px;">🔥 Featured Cover</div>
      <img src="/images/CACAIE.gif" alt="Large language model for post-earthquake structural damage assessment of buildings" width="100%">
    </div>
  </div>

  <div class="paper-box-text">

    <p>
      <a href="https://doi.org/10.1111/mice.70010">
        Large language model for post-earthquake structural damage assessment of buildings
      </a>
    </p>

    <p>
      <strong>Yongqing Jiang</strong>, Xinyi Shen, Jianze Wang, Kaoshan Dai
    </p>

    <p>
      <a href="https://doi.org/10.1111/mice.70010"><strong>Project</strong></a>
    </p>

    <ul>
      <li>
        We developed SDA-Chat, a multimodal Large Language Model (LLM) that automates professional post-earthquake structural damage assessment through multi-round vision-language interactions, achieving 83.04% accuracy with high inference efficiency.
      </li>
    </ul>

  </div>
</div>


<div class="paper-box">
  <div class="paper-box-image">
    <div>
      <div class="badge">Engineering Structure 2025</div>
      <img src="/images/ES_PFA.png" alt="A data-driven approach for predicting peak floor response based on visually observed rocking behaviors of freestanding NSCs" width="100%">
    </div>
  </div>

  <div class="paper-box-text">

    <p>
      <a href="https://doi.org/10.1016/j.engstruct.2025.120006">
        A data-driven approach for predicting peak floor response based on visually observed rocking behaviors of freestanding NSCs
      </a>
    </p>

    <p>
      <strong>Yongqing Jiang</strong>, Jianze Wang, Weiwei Chen, Kaoshan Dai
    </p>

    <p>
      <a href="https://doi.org/10.1016/j.engstruct.2025.120006"><strong>Project</strong></a>
    </p>

    <ul>
      <li>
        We propose a vision-based framework leveraging machine learning to infer Peak Floor Acceleration (PFA) ranges from the seismic responses of unanchored non-structural components, providing a cost-effective alternative to traditional monitoring with 84%–94% accuracy.
      </li>
    </ul>

  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image">
    <div>
      <div class="badge">Engineering Structure 2024</div>
      <img src="/images/ES_Video.png" alt="Video comprehension-based approach for seismic damage recognition of freestanding non-structural components" width="100%">
    </div>
  </div>

  <div class="paper-box-text">

    <p>
      <a href="https://doi.org/10.1016/j.engstruct.2024.118034">
        Video comprehension-based approach for seismic damage recognition of freestanding non-structural components
      </a>
    </p>

    <p>
      <strong>Yongqing Jiang</strong>, Jianze Wang, Xingquan Guan, Kaoshan Dai
    </p>

    <p>
      <a href="https://doi.org/10.1016/j.engstruct.2024.118034"><strong>Project</strong></a>
    </p>

    <ul>
      <li>
        We developed TPViT-DMSR, a customized two-pathway vision transformer designed to recognize the seismic damage states of freestanding non-structural components through video analysis, achieving a mean average precision of 74.87%.
      </li>
    </ul>

  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image">
    <div>
      <div class="badge">Automation in Construction 2021</div>
      <img src="/images/AIC_21.gif" alt="A deep learning approach for fast detection and classification of concrete damage" width="100%">
    </div>
  </div>

  <div class="paper-box-text">

    <p>
      <a href="https://doi.org/10.1016/j.engstruct.2024.118034">
        A deep learning approach for fast detection and classification of concrete damage
      </a>
    </p>

    <p>
      <strong>Yongqing Jiang</strong>, Dandan Pang, Chengdong Li
    </p>

    <p>
      <a href="https://doi.org/10.1016/j.engstruct.2024.118034"><strong>Project</strong></a>
    </p>

    <ul>
      <li>
        We developed TPViT-DMSR, a customized two-pathway vision transformer that leverages video-comprehension and trajectory attention to recognize the seismic damage states of freestanding non-structural components with a 74.87% mean average precision.
      </li>
    </ul>

  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image">
    <div>
      <div class="badge">Computer-Aided Civil and Infrastructure Engineering 2023</div>
      <img src="/images/CACAIE23.png" alt="A method of concrete damage detection and localization based on weakly supervised learning" width="100%">
    </div>
  </div>

  <div class="paper-box-text">

    <p>
      <a href="https://doi.org/10.1111/mice.13124">
        A method of concrete damage detection and localization based on weakly supervised learning
      </a>
    </p>

    <p>
      <strong>Yongqing Jiang</strong>, Dandan Pang, Chengdong Li, Jianze Wang
    </p>

    <p>
      <a href="https://doi.org/10.1111/mice.13124"><strong>Project</strong></a>
    </p>

    <ul>
      <li>
        We developed a CNN-based framework for automated concrete defect detection and sensor-free geographical localization, leveraging projection loss and feature vectorization to achieve pixel-level precision and 83.69% localization accuracy.
      </li>
    </ul>

  </div>
</div>

<div class="paper-box">
  <div class="paper-box-image">
    <div>
      <div class="badge">Engineering Structures 2023</div>
      <img src="/images/LSTM.png" alt="An adapted LSTM-DRRNet approach for predicting floor acceleration response spectrum" width="100%">
    </div>
  </div>

  <div class="paper-box-text">

    <p>
      <a href="https://doi.org/10.1016/j.engstruct.2023.116849">
        An adapted LSTM-DRRNet approach for predicting floor acceleration response spectrum
      </a>
    </p>

    <p>
      <strong>Yongqing Jiang</strong>, Dandan Pang, Chengdong Li, Jianze Wang
    </p>

    <p>
      <a href="https://doi.org/10.1016/j.engstruct.2023.116849"><strong>Project</strong></a>
    </p>

    <ul>
      <li>
        We developed a novel deep-learning framework integrating ACN-BiLSTM and DRRNet to provide generalized and efficient estimations of nonlinear floor response spectra with 97.29% accuracy, significantly advancing the seismic design and safety of non-structural components.
      </li>
    </ul>

  </div>
</div>


<div class="paper-box">
  <div class="paper-box-image">
    <div>
      <div class="badge">Engineering Applications of Artificial 2024</div>
      <div class="badge" style="background-color: #f39c12; top: 32px;">🔥 ESI Highly Cited</div>
      <img src="/images/EAAI.png" alt="Improved YOLOv8-GD deep learning model for defect detection in electroluminescence images of solar photovoltaic modules" width="100%">
    </div>
  </div>

  <div class="paper-box-text">

    <p>
      <a href="https://doi.org/10.1016/j.engappai.2024.107866">
        Improved YOLOv8-GD deep learning model for defect detection in electroluminescence images of solar photovoltaic modules
      </a>
    </p>

    <p>
      Yukang Cao, Dandan Pang, Qianchuan Zhao, Yi Yan, <strong>Yongqing Jiang</strong>, Chongyi Tian, Fan Wang, Junlin Li
    </p>

    <p>
      <a href="https://doi.org/10.1016/j.engappai.2024.107866"><strong>Project</strong></a>
    </p>

    <ul>
      <li>
        We propose <strong>YOLOv8-GD</strong>, a lightweight and accurate defect detection algorithm that optimizes the backbone with DW-Conv and GSConv, and incorporates a BiFPN structure, achieving a <strong>16.7% reduction</strong> in model size while improving mAP@0.5 by <strong>4.2%</strong>.
      </li>
    </ul>

  </div>
</div>


# 🎖 Honors and Awards
- *2025* Nominee for the Young Elite Scientist Sponsorship Program (**PhD Student Special Track**)
- *2025* Sichuan University PhD Innovation Scholarship (**Top 1%**).
- *2024* Sichuan University PhD Innovation Scholarship (**Top 1%**).
- *2024* Outstanding Graduate of Sichuan University (**Top 1%**).
- *2024* Sichuan University First-Class Scholarship (**Ranked 1st in Major**).
- *2022* National Scholarship by Ministry of Education of China (**Top 1%**).
- *2021* Outstanding Graduate of Shandong Province (**Top 1%**).
- *2021* First Prize of Outstanding Graduate Achievement Award in Shandong Province (**Top 3%**).

# 🏆 Competitions
- *2025* National Second Prize, Inaugural China Graduate Intelligent Construction Innovation Competition (Competition Entry: Intelligent Seismic Damage Identification and Assessment Technology for Buildings) (**Leader**) 
- *2021* Regional Third Prize (North China) the China Graduate Electronic Design Competition (Competition Entry: Real-time Portable Concrete Defect Detection System based on YOLOv4) (**Leader**)

[//]: # (# 📖 Educations)

[//]: # (- *2019.06 - 2022.04 &#40;now&#41;*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )

[//]: # (- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. )

# 💬 Invited Talks
- *2024.04*, A data-driven approach for estimating peak floor response based on damage of non-structural components." The 4th International Conference on Vulnerability and Risk Analysis and Management (ICVRAM-ISUMA 2024), Tongji University, Shanghai, China.
- *2023.08*, The 2nd Workshop on Big Data in Civil Engineering." Zhejiang University, Hangzhou, China. 
- *2023.05*, "The 3rd Academic Conference on Computational and Simulation Technologies in Civil Engineering." Guangxi University, Nanning, China.

# 🚀 Projects
- Intelligent Recognition of Indoor Seismic Damage Characteristics and Building Resilience Assessment Based on Video Understanding (National Natural Science Foundation of China, Young Scientists Fund; **_Key Researcher_**)
- Mechanisms and Applications of Fiber Bragg Grating–Based Acoustic Emission Sensing for Concrete Durability Damage Monitoring (National Natural Science Foundation of China, General Program; **_Key Researcher_**)
- Multi-Model Ensemble–Driven Precise Profiling of Office Building Operational States and Integrated Energy-Efficiency Optimization (National Natural Science Foundation of China, General Program; **_Key Researcher_**)
- Swarm-Intelligence–Based Bio-Inspired Control of Robotic Fish Schools for Navigation in Unknown Aquatic Environments (National Natural Science Foundation of China, General Program; **_Key Researcher_**)
- Coupled Optimization and Dual Control of Vibration and Wind-Induced Responses for Novel Structural Systems of Ultra-High Wind Power Towers (National Natural Science Foundation of China, General Program; **_Key Researcher_**)
- Outstanding Young Innovation Team in Artificial Intelligence and Building Intelligence, Shandong Provincial Higher Education Institutions (**_Key Researcher_**)

[//]: # (# 💻 Internships)

[//]: # (- *2019.05 - 2020.02*, [Lorem]&#40;https://github.com/&#41;, China.)