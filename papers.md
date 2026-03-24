---
title: ADMI 2026 Papers and Posters
---

<style>
:root {
  --bg: #0f172a;
  --panel: #111827;
  --soft: #1f2937;
  --border: #334155;
  --text: #e5e7eb;
  --muted: #94a3b8;
  --link: #93c5fd;
  --accent: #22c55e;
  --accent2: #a78bfa;
}
body {
  line-height: 1.55;
}
.page-wrap {
  max-width: 1200px;
  margin: 0 auto;
}
.hero {
  padding: 1.2rem 1.4rem;
  border: 1px solid var(--border);
  border-radius: 18px;
  background: linear-gradient(180deg, rgba(148,163,184,.08), rgba(15,23,42,.2));
  margin: 1rem 0 1.5rem;
}
.hero p { margin: .35rem 0; }
.quick-links, .tag-cloud, .filters {
  display: flex;
  flex-wrap: wrap;
  gap: .55rem;
  margin: .85rem 0;
}
.quick-links a, .tag-cloud a, .filter-btn {
  display: inline-block;
  padding: .42rem .75rem;
  border-radius: 999px;
  border: 1px solid var(--border);
  background: var(--soft);
  text-decoration: none;
  font-size: .95rem;
}
.filter-btn {
  color: inherit;
  cursor: pointer;
}
.filter-btn.active {
  border-color: var(--link);
  box-shadow: 0 0 0 1px rgba(147,197,253,.3) inset;
}
.filter-panel {
  position: sticky;
  top: .75rem;
  z-index: 20;
  background: rgba(15,23,42,.9);
  backdrop-filter: blur(8px);
  border: 1px solid var(--border);
  border-radius: 18px;
  padding: 1rem;
  margin: 1rem 0 1.5rem;
}
.searchbox {
  width: 100%;
  padding: .8rem .95rem;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: var(--panel);
  color: inherit;
  font-size: 1rem;
  box-sizing: border-box;
}
.section-block {
  margin: 2rem 0;
}
.category-block {
  margin: 1.4rem 0 2rem;
}
.category-meta {
  color: var(--muted);
  margin-top: -.35rem;
}
.paper-list {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin-top: 1rem;
}
.paper-card {
  border: 1px solid var(--border);
  border-radius: 18px;
  background: rgba(17,24,39,.72);
  padding: 1rem 1rem 1.1rem;
}
.paper-card h4 {
  margin: 0 0 .5rem;
  line-height: 1.3;
}
.paper-meta {
  color: var(--muted);
  font-size: .96rem;
  margin: .2rem 0;
}
.badges {
  display: flex;
  flex-wrap: wrap;
  gap: .45rem;
  margin: .75rem 0;
}
.badge {
  display: inline-block;
  border-radius: 999px;
  padding: .25rem .6rem;
  font-size: .84rem;
  border: 1px solid var(--border);
  background: var(--soft);
}
.badge.fulloral { border-color: rgba(34,197,94,.5); }
.badge.poster { border-color: rgba(167,139,250,.55); }
details {
  margin-top: .7rem;
  border-top: 1px dashed var(--border);
  padding-top: .7rem;
}
summary {
  cursor: pointer;
  color: var(--link);
}
.abstract {
  margin-top: .7rem;
  white-space: pre-wrap;
}
.small-note {
  color: var(--muted);
  font-size: .92rem;
}
.hidden-by-filter {
  display: none !important;
}
.section-anchor {
  scroll-margin-top: 7rem;
}
@media (min-width: 960px) {
  .paper-list {
    grid-template-columns: 1fr 1fr;
  }
}
</style>

<div class="page-wrap">

# ADMI 2026 Papers and Posters

<div class="hero">
  <p><strong>Browse the ADMI 2026 accepted submissions</strong> by presentation type and author category. Titles link to PDFs when a file is available under the repository's <code>sorted_papers</code> directory.</p>
  <p class="small-note">This page is designed for GitHub Pages and includes quick navigation, client-side search, tag-based filtering, and collapsible abstracts.</p>
</div>

## Quick navigation

<div class="quick-links">
<a href="#full-oral-papers">Full-Oral Papers</a>
<a href="#posters">Posters</a>
<a href="#full-oral-faculty">Faculty</a>
<a href="#full-oral-student-graduate">Student - Graduate</a>
<a href="#full-oral-student-undergraduate">Student - Undergraduate</a>
<a href="#poster-student-graduate">Student - Graduate</a>
<a href="#poster-student-undergraduate">Student - Undergraduate</a>
</div>

## Browse by tag

<div class="tag-cloud">
<a href="javascript:void(0)" class="tag-trigger" data-filter="All">All</a>
<a href="javascript:void(0)" class="tag-trigger" data-filter="Full-Oral">Full-Oral</a>
<a href="javascript:void(0)" class="tag-trigger" data-filter="Poster">Poster</a>
<a href="javascript:void(0)" class="tag-trigger" data-filter="Faculty">Faculty</a>
<a href="javascript:void(0)" class="tag-trigger" data-filter="Student - Graduate">Student - Graduate</a>
<a href="javascript:void(0)" class="tag-trigger" data-filter="Student - Undergraduate">Student - Undergraduate</a>
</div>

<div class="filter-panel">
  <input id="searchInput" class="searchbox" type="text" placeholder="Search titles, authors, abstracts, categories, and tags..." />
  <div class="filters" aria-label="Filter submissions">
    <button class="filter-btn active" data-filter="All">All</button>
    <button class="filter-btn" data-filter="Full-Oral">Full-Oral</button>
    <button class="filter-btn" data-filter="Poster">Poster</button>
    <button class="filter-btn" data-filter="Faculty">Faculty</button>
    <button class="filter-btn" data-filter="Student - Graduate">Student - Graduate</button>
    <button class="filter-btn" data-filter="Student - Undergraduate">Student - Undergraduate</button>
  </div>
  <p class="small-note"><span id="resultsCount">92</span> submissions shown.</p>
</div>

<div class="section-block section-anchor" id="full-oral-papers">

## Full-Oral Papers


<p class="small-note">28 submissions in this section.</p>

<div class="category-block section-anchor" id="full-oral-faculty">

### Faculty


<p class="category-meta">12 submissions</p>

<div class="paper-list">

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="exploring calculus concepts with maple somasundaram velummylum in calculus, we study techniques for finding the maximum and minimum values of functions, as well as evaluating and visualizing volumes of solids of revolution formed by rotating regions bounded by graphs over given intervals about horizontal or vertical axes. these concepts will be explored through illustrative examples using maple. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_12.pdf">EXPLORING CALCULUS CONCEPTS WITH MAPLE</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Somasundaram Velummylum</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">In calculus, we study techniques for finding the maximum
and minimum values of functions, as well as evaluating and
visualizing volumes of solids of revolution formed by
rotating regions bounded by graphs over given intervals
about horizontal or vertical axes. These concepts will be
explored through illustrative examples using MAPLE.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="an optimized artificial intelligence powered ios mobile app for weed identification biswajit biswal, jackson edwards weeds are a major burden in small and local farming communities in the united states due to the lack of technology, awareness, and education. weed control is one of the biggest factors that affects crop production. manual weeding gives maximum unique control of the weeds in the field. however, manual weeding has high labor intensity and high labor costs. this makes weed management difficult for small and local farmers in the state of south carolina, resulting in loss of crop yield and poor quality production. in this work, the ai-based ios mobile app is used to identify weed plants. in our work, we have successfully implemented an ios mobile app to capture a weed image and identifies weed-type using cnn, createml, xcode and swift programming language. our model was tested with our database of weed plants with a precision of 96%. our results show that the ios mobile app developed successfully identifies the weed plant. our future work will include testing the ios mobile app with more weed plant data to provide precise weed identification. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_13.pdf">An Optimized Artificial Intelligence Powered iOS Mobile App
for Weed Identification</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Biswajit Biswal, Jackson Edwards</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Weeds are a major burden in small and local farming
communities in the United States due to the lack of
technology, awareness, and education. Weed control is one
of the biggest factors that affects crop production. Manual
weeding gives maximum unique control of the weeds in the
field. However, manual weeding has high labor intensity and
high labor costs. This makes weed management difficult for
small and local farmers in the state of South Carolina,
resulting in loss of crop yield and poor quality
production. In this work, the AI-based iOS mobile app is
used to identify weed plants. In our work, we have
successfully implemented an iOS mobile app to capture a
weed image and identifies weed-type using CNN, CreateML,
Xcode and Swift programming language. Our model was tested
with our database of weed plants with a precision
of 96%. Our results show that the iOS mobile app developed
successfully identifies the weed plant. Our future work
will include testing the iOS mobile app with more weed
plant data to provide precise weed identification.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="enhancing computer science education through ai-driven scaffolding denny czejdo this paper presents a methodology for utilizing large language models (llms) to create ai-driven scaffolding materials in computer science. as enrollment in online and hybrid courses grows, the capacity for instructors to provide individual guidance to learners diminishes. this study introduces the &quot;a-h pedagogical framework,&quot; grounded in cognitive load theory and scaffolding principles. the methodology utilizes a human-in-the-loop ai workflow to analyze legacy educational materials (e.g., jupyter notebooks, pdfs), identify content and delivery method, and then propose improvements based on the &quot;a-h pedagogical framework.&quot; through a case study of gis data-processing assignments, this framework demonstrates how ai can enhance student learning by providing step-by-step, scaffolded guidance while reducing instructors&#x27; workload. the ai-driven approach enables scalable education and fosters learning experiences that are otherwise unattainable in large online classes. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_24.pdf">Enhancing Computer Science Education through AI-Driven
Scaffolding</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Denny Czejdo</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This paper presents a methodology for utilizing Large
Language Models (LLMs) to create AI-driven scaffolding
materials in Computer Science. As enrollment in online and
hybrid courses grows, the capacity for instructors to
provide individual guidance to learners diminishes. This
study introduces the &quot;A-H Pedagogical Framework,&quot; grounded
in cognitive load theory and scaffolding principles. The
methodology utilizes a Human-in-the-Loop AI workflow to
analyze legacy educational materials (e.g., Jupyter
Notebooks, PDFs), identify content and delivery method, and
then propose improvements based on the &quot;A-H Pedagogical
Framework.&quot; Through a case study of GIS Data-Processing
assignments, this framework demonstrates how AI can enhance
student learning by providing step-by-step, scaffolded
guidance while reducing instructors&#x27; workload. The
AI-driven approach enables scalable education and fosters
learning experiences that are otherwise unattainable in
large online classes.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="robust noise-resilient feature extract and 3d-cnn classification for hyperspectral imagery yan xu traditional hyperspectral image (hsi) classification relies on high-dimensional spectral signatures, often leading to the curse of dimensionality and high computational cost. most existing methods attempt to mitigate this by selecting dozens of bands; in this paper, we propose a highly efficient framework restricted to only three spectral bands. to maximize the information extracted from this minimal spectral subset, we employ a 3d convolutional neural network (3d-cnn) to capture joint spatial-spectral features. we investigate the efficacy of noise-adjusted principal component analysis (napca) as a dimensionality reduction tool, comparing it against standard principal component analysis (pca), incremental pca, unsupervised and supervised band selection methods. furthermore, we implement a spatial data augmentation strategy by integrating rotations and flips to artificially expand the training set and improve model generalization. experimental results on three real-world hsi datasets show the proposed approach shows superior performance compared with other state-of-the-art methods. this approach indicates a robust solution for resource-constrained remote sensing applications. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_25.pdf">Robust Noise-Resilient Feature Extract and 3D-CNN
classification for Hyperspectral imagery</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Yan Xu</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge"></span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Traditional hyperspectral image (HSI) classification relies
on high-dimensional spectral signatures, often leading to
the curse of dimensionality and high computational cost.
Most existing methods attempt to mitigate this by selecting
dozens of bands; In this paper, we propose a highly
efficient framework restricted to only three spectral
bands. To maximize the information extracted from this
minimal spectral subset, we employ a 3D Convolutional
Neural Network (3D-CNN) to capture joint spatial-spectral
features. We investigate the efficacy of Noise-Adjusted
Principal Component Analysis (NAPCA) as a dimensionality
reduction tool, comparing it against standard Principal
Component Analysis (PCA), Incremental PCA, unsupervised and
supervised band selection methods. Furthermore, we
implement a spatial data augmentation strategy by
integrating rotations and flips to artificially expand the
training set and improve model generalization. Experimental
results on three real-world HSI datasets show the proposed
approach shows superior performance compared with other
state-of-the-art methods. This approach indicates a robust
solution for resource-constrained remote sensing
applications.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="some experimental results for fingerprint image processing xiqiang zheng fingerprints offer a reliable and unique means of identification and hence are crucial in fields such as law enforcement and personal identification. however, fingerprint images are hardly of good quality. they may be corrupted and degraded with elements of noise owing to many issues including deviations in skin and impression circumstances. we test some commonly available fingerprint image processing codes and show some experimental results to see the progress and challenges of fingerprint image enhancement, segmentation and minutiae extraction. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_27.pdf">Some experimental results for fingerprint image processing</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Xiqiang Zheng</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Fingerprints offer a reliable and unique means of
identification and hence are crucial in fields such as law
enforcement and personal identification. However,
fingerprint images are hardly of good quality. They may be
corrupted and degraded with elements of noise owing to many
issues including deviations in skin and impression
circumstances. We test some commonly available fingerprint
image processing codes and show some experimental results
to see the progress and challenges of fingerprint image
enhancement, segmentation and minutiae extraction.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="robust noise-resilient feature extraction and 3d-cnn classification for hyperspectral imagery yan xu hyperspectral image (hsi) classification relies on high-dimensional spectral signatures, often leading to the curse of dimensionality and high computational cost. most existing methods attempt to mitigate this by selecting dozens of bands; in this paper, we propose a highly efficient framework that uses only three spectral bands. to maximize the information extracted from this minimal spectral subset, we employ a 3d convolutional neural network (3d-cnn) to capture joint spatial-spectral features. we investigate the efficacy of noise-adjusted principal component analysis (napca) as a dimensionality reduction tool, comparing it against standard principal component analysis (pca), incremental pca, unsupervised and supervised band selection methods. furthermore, we implement a spatial data augmentation strategy by integrating rotations and flips to artificially expand the training set and improve model generalization. experimental results on three real-world hsi datasets show that the proposed approach outperforms other state-of-the-art methods. this approach provides a robust solution for resource-constrained remote sensing applications. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_50.pdf">Robust Noise-Resilient Feature Extraction and 3D-CNN
Classification for Hyperspectral Imagery</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Yan Xu</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Hyperspectral image (HSI) classification relies on
high-dimensional spectral signatures, often leading to the
curse of dimensionality and high computational cost. Most
existing methods attempt to mitigate this by selecting
dozens of bands; in this paper, we propose a highly
efficient framework that uses only three spectral bands. To
maximize the information extracted from this minimal
spectral subset, we employ a 3D Convolutional Neural
Network (3D-CNN) to capture joint spatial-spectral
features. We investigate the efficacy of Noise-Adjusted
Principal Component Analysis (NAPCA) as a dimensionality
reduction tool, comparing it against standard Principal
Component Analysis (PCA), Incremental PCA, unsupervised and
supervised band selection methods. Furthermore, we
implement a spatial data augmentation strategy by
integrating rotations and flips to artificially expand the
training set and improve model generalization. Experimental
results on three real-world HSI datasets show that the
proposed approach outperforms other state-of-the-art
methods. This approach provides a robust solution for
resource-constrained remote sensing applications.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="using personalized generative ai as a “first responder” in c++ education to improve student learning sonya dennis, juana mendenhall using generative ai in the classroom to improve student learning requires deliberate, structured integration into course activities and assessments. this paper explores the integration of a specialized generative ai mentor, dennis ai, into three sections of an undergraduate computer programming ii course. the mentor was developed in conjunction with ibl.ai, a family-owned and operated company located in the technological hub of new york that specializes in building ai-driven, revenue-generating systems for the educational sector, serving learners from over 400 universities. the research evaluates a pedagogical shift from traditional passive learning to an active, generative model where ai serves as a &quot;first responder&quot; for complex technical concepts like memory management and object-oriented design. by leveraging the ibl.ai platform to synthesize course-specific data, the study demonstrates how structured prompt-based inquiry and iterative code generation can bridge the &quot;complexity wall&quot; often encountered in mid-level computer science curricula[1]. furthermore, the study illustrates how the integration of ai mentors and digital avatars---mapped to bloom&#x27;s taxonomy 4.0---facilitates a scalable model for high-level architectural mentoring and diagnostic practice[2]. ultimately, this study posits that the strategic deployment of specialized generative ai tools creates a dynamic environment that encourages deep inquiry, competitive innovation, and a rigorous validation process that preserves academic integrity. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_73.pdf">Using Personalized Generative AI as a “First Responder” in
C++ Education to improve student learning</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Sonya Dennis, Juana Mendenhall</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Using Generative AI in the classroom to improve student
learning requires deliberate, structured integration into
course activities and assessments. This paper explores the
integration of a specialized Generative AI mentor, Dennis
AI, into three sections of an undergraduate Computer
Programming II course. The mentor was developed in
conjunction with ibl.ai, a family-owned and operated
company located in the technological hub of New York that
specializes in building AI-driven, revenue-generating
systems for the educational sector, serving learners from
over 400 universities. The research evaluates a pedagogical
shift from traditional passive learning to an active,
generative model where AI serves as a &quot;First Responder&quot; for
complex technical concepts like memory management and
object-oriented design. By leveraging the ibl.ai platform
to synthesize course-specific data, the study demonstrates
how structured prompt-based inquiry and iterative code
generation can bridge the &quot;complexity wall&quot; often
encountered in mid-level computer science curricula[1].
Furthermore, the study illustrates how the integration of
AI mentors and digital avatars---mapped to Bloom&#x27;s Taxonomy
4.0---facilitates a scalable model for high-level
architectural mentoring and diagnostic practice[2].
Ultimately, this study posits that the strategic deployment
of specialized Generative AI tools creates a dynamic
environment that encourages deep inquiry, competitive
innovation, and a rigorous validation process that
preserves academic integrity.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="the importance of course redesign: microlearning strategies for enhanced course design: insights from the jcsu citl summer workshop sonya worrell sonya worrell this article explores innovative course design strategies aimed at enhancing student engagement and learning retention, informed by insights gained during the jcsu citl summer course design workshop held from june 2nd to the 4th, 2025. specifically tailored for stem faculty, the workshop emphasized integrating microlearning techniques, modular course structures, and establishing instructor presence. this paper discusses key takeaways, practical strategies, and the implications of these approaches for improving educational experiences. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_74.pdf">The Importance of Course Redesign:  Microlearning
Strategies for Enhanced Course Design: Insights from the
JCSU CITL Summer Workshop</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Sonya Worrell Sonya Worrell</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This article explores innovative course design strategies
aimed at enhancing student engagement and learning
retention, informed by insights gained during the JCSU CITL
Summer Course Design Workshop held from June 2nd to the
4th, 2025. Specifically tailored for STEM faculty, the
workshop emphasized integrating microlearning techniques,
modular course structures, and establishing instructor
presence. This paper discusses key takeaways, practical
strategies, and the implications of these approaches for
improving educational experiences.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="developing effective computer science program curricula and ai-driven educational models to enhance learning outcomes deok nam the rapid evolution of artificial intelligence (ai) and computing technologies has fundamentally reshaped workforce demands, necessitating a transformation in how computer science (cs) education is designed and delivered. traditional cs curricula often struggle to keep pace with industry innovation, provide personalized learning experiences, and equitably support diverse learner populations. this paper presents a comprehensive framework for developing effective computer science program curricula integrated with ai-driven educational models to enhance student learning outcomes. the proposed approach aligns curriculum design with competency-based education, industry relevance, and adaptive ai technologies such as intelligent tutoring systems, learning analytics, and personalized content recommendation. through curriculum mapping, instructional design models, and ai-enabled assessment strategies, the paper demonstrates how ai can improve student engagement, mastery, retention, and employability. a case-based implementation model and evaluation metrics are presented to guide institutions in adopting scalable, ethical, and inclusive ai-enhanced cs education. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_79.pdf">Developing Effective Computer Science Program Curricula and
AI-Driven Educational Models to Enhance Learning Outcomes</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Deok Nam</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The rapid evolution of artificial intelligence (AI) and
computing technologies has fundamentally reshaped workforce
demands, necessitating a transformation in how computer
science (CS) education is designed and delivered.
Traditional CS curricula often struggle to keep pace with
industry innovation, provide personalized learning
experiences, and equitably support diverse learner
populations. This paper presents a comprehensive framework
for developing effective computer science program curricula
integrated with AI-driven educational models to enhance
student learning outcomes. The proposed approach aligns
curriculum design with competency-based education, industry
relevance, and adaptive AI technologies such as intelligent
tutoring systems, learning analytics, and personalized
content recommendation. Through curriculum mapping,
instructional design models, and AI-enabled assessment
strategies, the paper demonstrates how AI can improve
student engagement, mastery, retention, and employability.
A case-based implementation model and evaluation metrics
are presented to guide institutions in adopting scalable,
ethical, and inclusive AI-enhanced CS education.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="enhancing data mining and machine learning course by using hpc mohamed elbakary, sheryl bradford a data mining and machine learning course is offered in spring at elizabeth city state university. the course covers the most important data mining and analysis techniques and provides background knowledge on how to conduct a data mining project. after defining what knowledge discovery and data mining are, data mining tasks such as classification, clustering, and association analysis will be discussed in detail. basic data analysis techniques, centering on basic visualization techniques and statistics, to get a better understanding of the data mining task at hand will be covered. moreover, techniques on how to preprocess a data set for a data mining task will be introduced. also, in course projects students will obtain hands-on experience in conducting data mining and data analysis projects. in addition, fundamentals of machine learning such as neural network and deep learning will be introduced. we introduce an enhancement for the course material by incorporating hpc in implementation of the ml algorithms such as k-mean algorithm. full-oral faculty full-oral">
  <h4>Enhancing Data Mining and Machine Learning Course by Using
HPC</h4>
  <div class="paper-meta"><strong>Authors:</strong> Mohamed Elbakary, Sheryl Bradford</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">A data mining and machine learning course is offered in
spring at Elizabeth City State University. The course
covers the most important data mining and analysis
techniques and provides background knowledge on how to
conduct a data mining project. After defining what
knowledge discovery and data mining are, data mining tasks
such as classification, clustering, and association
analysis will be discussed in detail. Basic data analysis
techniques, centering on basic visualization techniques and
statistics, to get a better understanding of the data
mining task at hand will be covered. Moreover, techniques
on how to preprocess a data set for a data mining task will
be introduced. Also, in course projects students will
obtain hands-on experience in conducting data mining and
data analysis projects. In addition, fundamentals of
Machine Learning such as neural Network and Deep Learning
will be introduced. we introduce an enhancement for the
course material by incorporating HPC in implementation of
the ML algorithms such as k-mean algorithm.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="findings from a feasibility study on ai-aligned experiential learning at an hbcu rose shumba building a pathway from ai coursework to ai careers requires a clear understanding of what students experience between the classroom and the job market. this paper reports results from a feasibility study supported by the university system of maryland elkins transformation award at bowie state university (bsu). the study examined barriers to student participation in ai-aligned experiential learning and assessed institutional readiness for scaling career-connected learning. the feasibility study gathered input from 200 students, 15 faculty members, and 10 industry partners to assess constraints, capacity, and partnership needs for expanding ai-aligned experiential learning. we describe the study methods and key findings, then discuss what they suggest about the importance of experiential learning centers as a strategy for strengthening ai workforce preparation at hbcus. the work builds on several years of experiential learning work, including a tech pipeline program featured in the new york times describing how bsu developed employer partnerships to strengthen student career outcomes. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_91.pdf">Findings from a Feasibility Study on AI-Aligned
Experiential Learning at an HBCU</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Rose Shumba</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Building a pathway from AI coursework to AI careers
requires a clear understanding of what students experience
between the classroom and the job market. This paper
reports results from a feasibility study supported by the
University System of Maryland Elkins Transformation Award
at Bowie State University (BSU). The study examined
barriers to student participation in AI-aligned
experiential learning and assessed institutional readiness
for scaling career-connected learning. The feasibility
study gathered input from 200 students, 15 faculty members,
and 10 industry partners to assess constraints, capacity,
and partnership needs for expanding AI-aligned experiential
learning. We describe the study methods and key findings,
then discuss what they suggest about the importance of
experiential learning centers as a strategy for
strengthening AI workforce preparation at HBCUs. The work
builds on several years of experiential learning work,
including a Tech Pipeline Program featured in The New York
Times describing how BSU developed employer partnerships to
strengthen student career outcomes.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Faculty" data-search="building the next generation of cyber ai professionals: lessons from bowie state university’s cyberai scholarship for service program rose shumba the cyberaicorps scholarship for service (cyberai sfs), formerly the cybercorps® scholarship for service (sfs), supports cybersecurity education in exchange for post-graduation government service. this paper describes bowie state university’s cyberai sfs program and shares early lessons from implementation since 2023. the program has supported 14 scholars and has strengthened recruitment by offering a funded, structured pathway into government cybersecurity careers. we summarize the student experience and program operations, including cohort support, mentoring, professional development, certifications preparation, research and conference participation, and structured preparation for internships and government employment. we report outcomes in aggregate, including internship placements and early cybersecurity-related government employment, and highlight the operational choices that helped students participate fully while meeting program requirements. the paper concludes with takeaways for hbcus exploring cyberai sfs participation and an invitation to an april 2026 virtual workshop for institutions interested in joining as mentoring partners and building toward future readiness. full-oral faculty full-oral">
  <h4><a href="sorted_papers/Full-Oral/Faculty/ADMI_2026_paper_92.pdf">Building the Next Generation of Cyber AI Professionals:
Lessons from Bowie State University’s CyberAI Scholarship
For Service Program</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Rose Shumba</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Faculty</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The CyberAICorps Scholarship for Service (CyberAI SFS),
formerly the CyberCorps® Scholarship for Service (SFS),
supports cybersecurity education in exchange for
post-graduation government service. This paper describes
Bowie State University’s CyberAI SFS program and shares
early lessons from implementation since 2023. The program
has supported 14 scholars and has strengthened recruitment
by offering a funded, structured pathway into government
cybersecurity careers. We summarize the student experience
and program operations, including cohort support,
mentoring, professional development, certifications
preparation, research and conference participation, and
structured preparation for internships and government
employment. We report outcomes in aggregate, including
internship placements and early cybersecurity-related
government employment, and highlight the operational
choices that helped students participate fully while
meeting program requirements. The paper concludes with
takeaways for HBCUs exploring CyberAI SFS participation and
an invitation to an April 2026 virtual workshop for
institutions interested in joining as mentoring partners
and building toward future readiness.</div>
  </details>
</article>

</div>
</div>

<div class="category-block section-anchor" id="full-oral-student-graduate">

### Student - Graduate


<p class="category-meta">8 submissions</p>

<div class="paper-list">

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Graduate" data-search="forgetting by design: testing the effectiveness of machine unlearning in right to be forgotten data deletion jericka guy, chutima boonthum-denecke the right to be forgotten (rtbf) is a legal requirement that allows individuals to request the deletion of their personal data from digital systems. however, in modern machine learning environments, fully removing data is technically challenging once it has been incorporated into trained models. this research investigates whether machine unlearning can serve as an effective mechanism for supporting rtbf by removing the influence of specific data from a trained model. the study evaluates a pre-trained neural network using multiple forget set sizes and applies membership inference attacks (mia) to measure whether deleted data remains detectable after unlearning. experimental results show that while machine unlearning preserves performance on retained data, it does not fully eliminate the influence of forgotten data, as residual information remains detectable across all tested configurations. these findings demonstrate that machine unlearning alone is insufficient to guarantee complete data deletion and highlight the need for stronger verification methods and complementary strategies to support rtbf compliance in ai systems. full-oral student - graduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Graduate/ADMI_2026_paper_6.pdf">FORGETTING BY DESIGN: TESTING THE EFFECTIVENESS OF MACHINE
UNLEARNING IN RIGHT TO BE FORGOTTEN DATA DELETION</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Jericka Guy, Chutima Boonthum-Denecke</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The Right to Be Forgotten (RTBF) is a legal requirement
that allows individuals to request the deletion of their
personal data from digital systems. However, in modern
machine learning environments, fully removing data is
technically challenging once it has been incorporated into
trained models. This research investigates whether machine
unlearning can serve as an effective mechanism for
supporting RTBF by removing the influence of specific data
from a trained model. The study evaluates a pre-trained
neural network using multiple forget set sizes and applies
Membership Inference Attacks (MIA) to measure whether
deleted data remains detectable after unlearning.
Experimental results show that while machine unlearning
preserves performance on retained data, it does not fully
eliminate the influence of forgotten data, as residual
information remains detectable across all tested
configurations. These findings demonstrate that machine
unlearning alone is insufficient to guarantee complete data
deletion and highlight the need for stronger verification
methods and complementary strategies to support RTBF
compliance in AI systems.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Graduate" data-search="sql injection prevention techniques angela darden, chutima boonthum-denecke sql injections are one of the most common and dangerous vulnerabilities found in web applications, even though they have been well documented for decades. this paper explores the effectiveness of common prevention techniques against sql injection attacks, including input validation, parameterized queries, and prepared statements. to demonstrate, a vulnerable web environment was created using damn vulnerable web application (dvwa) to simulate attacks and observe how each defense method withstands different injection attempts. the results will show the strengths and weaknesses of each approach when tested against real-world attack patterns. in addition to testing, this research highlights the relevance of sql injections in today’s cybersecurity environment, shown by their inclusion in the owasp top 10 [4]. by demonstrating how easily unsecured applications can become victims of attacks and how effective proper countermeasures can be, this paper highlights the importance of implementing secure coding practices in modern web development. full-oral student - graduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Graduate/ADMI_2026_paper_7.pdf">SQL Injection Prevention Techniques</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Angela Darden, Chutima Boonthum-Denecke</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">SQL injections are one of the most common and dangerous
vulnerabilities found in web applications, even though they
have been well documented for decades. This paper explores
the effectiveness of common prevention techniques against
SQL injection attacks, including input validation,
parameterized queries, and prepared statements. To
demonstrate, a vulnerable web environment was created using
Damn Vulnerable Web Application (DVWA) to simulate attacks
and observe how each defense method withstands different
injection attempts. The results will show the strengths and
weaknesses of each approach when tested against real-world
attack patterns. In addition to testing, this research
highlights the relevance of SQL injections in today’s
cybersecurity environment, shown by their inclusion in the
OWASP Top 10 [4]. By demonstrating how easily unsecured
applications can become victims of attacks and how
effective proper countermeasures can be, this paper
highlights the importance of implementing secure coding
practices in modern web development.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Graduate" data-search="a hands-on laboratory approach to supporting student learning in computer vision education terrelle thomas, idongesit mkpong-ruffin, chutima boonthum-denecke, deidre evans as artificial intelligence increases and is used in daily life activi-ties, the need to understand and interact with artificial intelligence has become important and is now emphasized in undergraduate and graduate programs. even though ai is being taught, some top-ics such as computer vision (detr, yolov8, faster r-cnn, and ssd) remain difficult for students to understand and incorporate into practice. without a definite percentage indicating how many students are affected, current discussions continue to show that computer vision is one of the topics learners struggle to grasp [3]. to address these challenges, a structured framework of hands-on labs in computer vision can support students in strengthening their comprehension at both undergraduate and graduate levels. a hands-on lab is a structured learning activity in which students actively perform tasks, experiments, or problem-solving activities using tools, technologies, or data rather than relying solely on lec-tures. this experiential approach requires learners to interact with software, equipment, or real-world datasets to apply theoretical concepts in a practical context. hands-on labs help students un-derstand complex ai and computer vision topics by transforming abstract concepts such as convolution, feature extraction, and ob-ject detection pipelines into concrete, interactive experiences that enhance understanding. by working directly with detection mod-els like yolo, ssd, faster r-cnn, and detr, students develop stronger intuition, reduce cognitive overload, and build practical skills needed to apply these systems in real-world scenarios. prior research in computing and engineering education indicates that project-based and hands-on learning approaches significantly im-prove student comprehension, engagement, and overall learning outcomes [4]. full-oral student - graduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Graduate/ADMI_2026_paper_20.pdf">A Hands-On Laboratory Approach to Supporting Student
Learning in Computer Vision Education</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Terrelle Thomas, Idongesit Mkpong-Ruffin, Chutima Boonthum-Denecke, Deidre Evans</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">As artificial intelligence increases and is used in daily
life activi-ties, the need to understand and interact with
artificial intelligence has become important and is now
emphasized in undergraduate and graduate programs. Even
though AI is being taught, some top-ics such as computer
vision (DETR, YOLOv8, Faster R-CNN, and SSD) remain
difficult for students to understand and incorporate into
practice. Without a definite percentage indicating how many
students are affected, current discussions continue to show
that computer vision is one of the topics learners struggle
to grasp [3]. To address these challenges, a structured
framework of hands-on labs in computer vision can support
students in strengthening their comprehension at both
undergraduate and graduate levels. A hands-on lab is a
structured learning activity in which students actively
perform tasks, experiments, or problem-solving activities
using tools, technologies, or data rather than relying
solely on lec-tures. This experiential approach requires
learners to interact with software, equipment, or
real-world datasets to apply theoretical concepts in a
practical context. Hands-on labs help students un-derstand
complex AI and computer vision topics by transforming
abstract concepts such as convolution, feature extraction,
and ob-ject detection pipelines into concrete, interactive
experiences that enhance understanding. By working directly
with detection mod-els like YOLO, SSD, Faster R-CNN, and
DETR, students develop stronger intuition, reduce cognitive
overload, and build practical skills needed to apply these
systems in real-world scenarios. Prior research in
computing and engineering education indicates that
project-based and hands-on learning approaches
significantly im-prove student comprehension, engagement,
and overall learning outcomes [4].</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Graduate" data-search="investigating motion-focused video frame interpolation: efficiency vs. fidelity carlos sac mendoza, lily liang, briana wellman a significant challenge in video frame interpolation (vfi) is reducing the processing time without significantly sacrificing visual quality. to address it, we developed a computationally efficient motion-focused vfi methodology, based on google&#x27;s film (frame interpolation for large motion) model. our proposed approach, motion-focused film, selectively interpolates only the most dynamic areas of the video to reduce the computational load and processing time. we also implemented a tensor bucketing strategy to reduce computational overhead. we evaluated our approach on the davis 2017 dataset. the results show a 95% reduction in processing time compared to the full-frame method. it achieved a peak signal-to-noise ratio (psnr) score that was approximately 88% of the baseline, indicating a discernible loss in pixel-level fidelity. however, it retained over 87% of the structural similarity (ssim) test, suggesting that the overall structure of the interpolated image remains mostly intact. we also investigated the impact of video resolution on our approach&#x27;s performance. full-oral student - graduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Graduate/ADMI_2026_paper_23.pdf">Investigating Motion-Focused Video Frame Interpolation:
Efficiency vs. Fidelity</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Carlos Sac Mendoza, Lily Liang, Briana Wellman</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">A significant challenge in Video Frame Interpolation (VFI)
is reducing the processing time without significantly
sacrificing visual quality. To address it, we developed a
computationally efficient motion-focused VFI methodology,
based on Google&#x27;s FILM (Frame Interpolation for Large
Motion) model. Our proposed approach, Motion-focused FILM,
selectively interpolates only the most dynamic areas of the
video to reduce the computational load and processing time.
We also implemented a tensor bucketing strategy to reduce
computational overhead.

    We evaluated our approach on the DAVIS 2017 dataset.
    The results show a 95% reduction in processing time
    compared to the full-frame method. It achieved a Peak
    Signal-to-Noise Ratio (PSNR) score that was
    approximately 88% of the baseline, indicating a
    discernible loss in pixel-level fidelity. However, it
    retained over 87% of the structural similarity (SSIM)
    test, suggesting that the overall structure of the
    interpolated image remains mostly intact. We also
    investigated the impact of video resolution on our
    approach&#x27;s performance.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Graduate" data-search="integrating blockchain dapp development in cybersecurity education via real-world applications javonte carter, inioluwa kola-adelakin, jerry miller, hongmei chi this paper presents a structured pedagogical framework for integrating blockchain decentralized application (dapp) development into cybersecurity education through experiential, project-based learning. the framework is implemented via a series of laboratory modules that immerse students in authentic, project-based activities grounded in real-world use cases, including blockchain-based diploma and transcript verification, cryptocurrency (bitcoin) forensic analysis, and secure supply chain management. through these activities, students gain practical exposure to distributed systems, smart contracts, and security mechanisms within blockchain environments. preliminary classroom outcomes demonstrate increased student interesting in learning dapp development, enhanced conceptual understanding of blockchain and cybersecurity principles, and improved preparedness for industry and research-oriented roles. overall, the proposed framework aims to (1) strengthen students’ skills and awareness of blockchain source code vulnerabilities, along with associated detection and mitigation techniques; (2) systematically integrate blockchain vulnerability concepts into information technology and cybersecurity curricula; and (3) prepare future it professionals with a solid understanding of blockchain attack surfaces and defensive strategies in real-world contexts. full-oral student - graduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Graduate/ADMI_2026_paper_51.pdf">Integrating Blockchain dApp Development in Cybersecurity
Education via Real-World Applications</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Javonte Carter, Inioluwa Kola-Adelakin, Jerry Miller, Hongmei Chi</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This paper presents a structured pedagogical framework for
integrating blockchain decentralized application (dApp)
development into cybersecurity education through
experiential, project-based learning. The framework is
implemented via a series of laboratory modules that immerse
students in authentic, project-based activities grounded in
real-world use cases, including blockchain-based diploma
and transcript verification, cryptocurrency (Bitcoin)
forensic analysis, and secure supply chain management.
Through these activities, students gain practical exposure
to distributed systems, smart contracts, and security
mechanisms within blockchain environments. Preliminary
classroom outcomes demonstrate increased student
interesting in learning dApp development, enhanced
conceptual understanding of blockchain and cybersecurity
principles, and improved preparedness for industry and
research-oriented roles. Overall, the proposed framework
aims to (1) strengthen students’ skills and awareness of
blockchain source code vulnerabilities, along with
associated detection and mitigation techniques; (2)
systematically integrate blockchain vulnerability concepts
into information technology and cybersecurity curricula;
and (3) prepare future IT professionals with a solid
understanding of blockchain attack surfaces and defensive
strategies in real-world contexts.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Graduate" data-search="advancing digital forensics with the integration of cyber threat intelligence technologies frank junior hoza longfor, yohn j parra bautista, adi chauhan, hongmei chi this research project explores a novel approach to bolstering digital forensics by integrating alienvault, a leading security platform, with blockchain technology. by harnessing the capabilities of alienvault for real-time threat detection and incident response and leveraging the immutable nature of blockchain for data integrity, this study proposes a framework for enhancing the reliability of digital forensic investigations. the tools used include alienvault’s open-source security information management (ossim) platform for security information and event management (siem). ethereum’s blockchain-based ledger is used to log events detected by alienvault ossim, ensuring each event log entry is time-stamped. data sources for this study include a controlled setup network and the open threat research (otrf) security dataset of windows event logs. these sources provide a comprehensive and realistic range of cyber-attack scenarios. by utilizing these datasets, the research evaluates how well the integrated system can detect and store threat information. the system’s performance is assessed based on its accuracy in identifying attacks, the speed of its incident response, and the reliability of its forensic data. the expected result is a blockchain-enhanced forensic framework that mitigates common challenges in digital forensics, such as data tampering and chain of custody issues. full-oral student - graduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Graduate/ADMI_2026_paper_85.pdf">Advancing Digital Forensics with the Integration of Cyber
Threat Intelligence Technologies</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Frank Junior Hoza Longfor, Yohn J Parra Bautista, Adi Chauhan, Hongmei Chi</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This research project explores a novel approach to
bolstering digital forensics by integrating AlienVault, a
leading security platform, with blockchain technology. By
harnessing the capabilities of AlienVault for real-time
threat detection and incident response and leveraging the
immutable nature of blockchain for data integrity, this
study proposes a framework for enhancing the reliability of
digital forensic investigations. The tools used include
AlienVault’s Open-Source Security Information Management
(OSSIM) platform for security information and event
management (SIEM). Ethereum’s blockchain-based ledger is
used to log events detected by AlienVault OSSIM, ensuring
each event log entry is time-stamped. Data sources for this
study include a controlled setup network and the Open
Threat Research (OTRF) Security Dataset of Windows event
logs. These sources provide a comprehensive and realistic
range of cyber-attack scenarios. By utilizing these
datasets, the research evaluates how well the integrated
system can detect and store threat information. The
system’s performance is assessed based on its accuracy in
identifying attacks, the speed of its incident response,
and the reliability of its forensic data. The expected
result is a blockchain-enhanced forensic framework that
mitigates common challenges in digital forensics, such as
data tampering and chain of custody issues.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Graduate" data-search="blockchain-enabled iot security: a distributed computing approach using dew and cloudlet architecture fahmina nur salma, md kamruzzaman sarker the integration of internet of things (iot) and blockchain technology presents significant opportunities to address critical security vulnerabilities in modern iot ecosystems. this paper investigates the challenges associated with implementing blockchain technology within iot environments and proposes a novel architectural framework leveraging dew and cloudlet computing paradigms. our approach addresses fundamental security issues including data integrity, privacy concerns, and the limitations of centralized iot architectures. by employing a three-layer architecture encompassing device, dew-blockchain, and cloudlet-blockchain layers, we demonstrate how distributed computing can enhance authentication efficiency, data processing, and storage services. the proposed framework utilizes blockchain&#x27;s inherent characteristics—decentralization, immutability, and auditability—to establish a secure, scalable foundation for iot applications across healthcare, smart cities, agriculture, and military domains. this research contributes to the evolving landscape of blockchain-iot integration by identifying implementation challenges, evaluating consensus mechanisms, and proposing practical solutions for real-world deployment. full-oral student - graduate full-oral">
  <h4>Blockchain-Enabled IoT Security: A Distributed Computing
Approach Using Dew and Cloudlet Architecture</h4>
  <div class="paper-meta"><strong>Authors:</strong> Fahmina Nur Salma, Md Kamruzzaman Sarker</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The integration of Internet of Things (IoT) and blockchain
technology presents significant opportunities to address
critical security vulnerabilities in modern IoT ecosystems.
This paper investigates the challenges associated with
implementing blockchain technology within IoT environments
and proposes a novel architectural framework leveraging dew
and cloudlet computing paradigms. Our approach addresses
fundamental security issues including data integrity,
privacy concerns, and the limitations of centralized IoT
architectures. By employing a three-layer architecture
encompassing device, dew-blockchain, and
cloudlet-blockchain layers, we demonstrate how distributed
computing can enhance authentication efficiency, data
processing, and storage services. The proposed framework
utilizes blockchain&#x27;s inherent
characteristics—decentralization, immutability, and
auditability—to establish a secure, scalable foundation for
IoT applications across healthcare, smart cities,
agriculture, and military domains. This research
contributes to the evolving landscape of blockchain-IoT
integration by identifying implementation challenges,
evaluating consensus mechanisms, and proposing practical
solutions for real-world deployment.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Graduate" data-search="bridging policy and practice: the class aligned framework for responsible ai integration in higher education joshua harrell, jeaime powell, dillon moore, qimora mason, suniyah esey, abraham ashade, linda hayden, mohamed elbakary the rapid expansion of artificial intelligence (ai), high-performance computing (hpc), and science gateway technologies in higher education has created new opportunities for experiential learning while introducing complexity for faculty seeking structured and policy-compliant integration. this paper presents the class aligned (course learning &amp; analytics support system) framework, a faculty-centered, governance-aware architecture designed to support the incorporation of ai, hpc, and science gateway technologies into undergraduate curricula. the framework connects institutional ai policy, structured instructional workflows, scalable computing infrastructure, and measurable learning analytics into a unified alignment model. using a design-based research approach, we describe the conceptual model, system architecture, and planned prototype implementation. the framework proposes embedding compliance logic and cyberinfrastructure guidance directly within ai-assisted workflows to reduce faculty uncertainty and translate institutional policy into actionable instructional practice. class aligned offers a scalable model for institutions seeking to expand ai- and hpc-enabled instruction while maintaining governance, reproducibility, and equitable access to advanced cyberinfrastructure resources. full-oral student - graduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Graduate/ADMI_2026_paper_90.pdf">Bridging Policy and Practice:  The CLASS AlignED Framework
for Responsible AI Integration in Higher Education</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Joshua Harrell, Jeaime Powell, Dillon Moore, Qimora Mason, Suniyah Esey, Abraham Ashade, Linda Hayden, Mohamed Elbakary</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The rapid expansion of artificial intelligence (AI),
high-performance computing (HPC), and Science Gateway
technologies in higher education has created new
opportunities for experiential learning while introducing
complexity for faculty seeking structured and
policy-compliant integration. This paper presents the CLASS
AlignED (Course Learning &amp; Analytics Support System)
Framework, a faculty-centered, governance-aware
architecture designed to support the incorporation of AI,
HPC, and Science Gateway technologies into undergraduate
curricula. The framework connects institutional AI policy,
structured instructional workflows, scalable computing
infrastructure, and measurable learning analytics into a
unified alignment model. Using a design-based research
approach, we describe the conceptual model, system
architecture, and planned prototype implementation. The
framework proposes embedding compliance logic and
cyberinfrastructure guidance directly within AI-assisted
workflows to reduce faculty uncertainty and translate
institutional policy into actionable instructional
practice. CLASS AlignED offers a scalable model for
institutions seeking to expand AI- and HPC-enabled
instruction while maintaining governance, reproducibility,
and equitable access to advanced cyberinfrastructure
resources.</div>
  </details>
</article>

</div>
</div>

<div class="category-block section-anchor" id="full-oral-student-undergraduate">

### Student - Undergraduate


<p class="category-meta">16 submissions</p>

<div class="paper-list">

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="machine learning-based detection of business email compromise: a comparative analysis of gradient boosting techniques philip baning business email compromise (bec) attacks constitute one of the most financially damaging cyber threats, resulting in global losses exceeding 2.7 billion usd annually according to the fbi internet crime complaint center. unlike conventional phishing attacks that deploy malicious payloads or urls, bec employs sophisticated social engineering via carefully crafted language, posing substantial challenges to traditional signaturebased detection systems. this work develops a robust machine learning framework for automated bec detection, incorporating 58 specialized features extracted from email content, metadata, and behavioral attributes. we provide a formal mathematical formulation of the feature extraction process and evaluate five gradient boosting algorithms—xgboost, lightgbm, catboost, random forest, and a stacking ensemble on the kaggle fraud email dataset (9,239 samples). the dataset undergoes an 80/20 stratified split to preserve class distribution. catboost attains the highest performance, with 97.29 percent accuracy, 97.29 percent f1 score, and 99.55 percent auc roc. we employ mcnemar’s test to confirm statistical significance (χ2 = 7.52, p &lt; 0.01) and utilize shap (shapley additive explanations) to isolate linguistic metrics specifically text entropy and readability—as primary discriminators. furthermore, we present a computational complexity analysis demonstrating that our pipeline operates with o(l) linear complexity relative to email length, achieving sub 10 ms inference latency suitable for real time siem integration. the framework outperforms existing benchmarks by 8.8 percent in f1 score, establishing a new baseline for content centric threat detection. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_1.pdf">Machine Learning-Based Detection of Business Email
Compromise: A Comparative Analysis of Gradient Boosting
Techniques</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Philip Baning</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Business Email Compromise (BEC) attacks constitute one of
the most financially damaging cyber threats, resulting in
global losses exceeding 2.7 billion USD annually according
to the FBI Internet Crime Complaint Center. Unlike
conventional phishing attacks that deploy malicious
payloads or URLs, BEC employs sophisticated social
engineering via carefully crafted language, posing
substantial challenges to traditional signaturebased
detection systems. This work develops a robust machine
learning framework for automated BEC detection,
incorporating 58 specialized features extracted from email
content, metadata, and behavioral attributes.

We provide a formal mathematical formulation of the feature
extraction process and evaluate five gradient boosting
algorithms—XGBoost, LightGBM, CatBoost, Random Forest, and
a stacking ensemble on the Kaggle Fraud Email Dataset
(9,239 samples). The dataset undergoes an 80/20 stratified
split to preserve class distribution. CatBoost attains the
highest performance, with 97.29 percent accuracy, 97.29
percent F1 score, and 99.55 percent AUC ROC. We employ
McNemar’s test to confirm statistical significance (χ2 =
7.52, p &lt; 0.01) and utilize SHAP (SHapley Additive
exPlanations) to isolate linguistic metrics specifically
text entropy and readability—as primary discriminators.
Furthermore, we present a computational complexity analysis
demonstrating that our pipeline operates with O(L) linear
complexity relative to email length, achieving sub 10 ms
inference latency suitable for real time SIEM integration.
The framework outperforms existing benchmarks by 8.8
percent in F1 score, establishing a new baseline for
content centric threat detection.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="ai and automation in sports ryan grimes, jean muhammad, chutima boonthum-denecke artificial intelligence (ai) and automation has been one of the most popular topics of the century. it has been integrated into education, medicine, and transportation to make tasks easier and increase productivity. ai and automation is constantly being discussed for being a double edged sword. on one side, it makes tasks capable of being completed faster and oftentimes more accurate, but the other side argues that it lacks accountability. before ai and automation is introduced to a system , it is integral to analyze the pros and cons of said implementation. this research focuses on the integration of ai and automation in sports and how its risks can affect athlete data, match outcomes, and device reliability. past research has examined accuracy and health benefits; however, device security, data flow, and contingency planning in the event of an attack or breach has not been acknowledged. this study investigates these gaps by examining how ai-driven wearables and automated officiating systems function; how data flow is mapped; and what vulnerabilities affect confidentiality, integrity, and availability. literature reviews and input from sports management and computer science professionals, athletes, and trainers will illustrate what protections are currently available and what they think of the trade-offs. the results will highlight key risks, identify potential solutions, and offer guidance for sports organizations and tech developers so that ai and automation in sports can be both innovative and secure. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_4.pdf">AI and Automation in Sports</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Ryan Grimes, Jean Muhammad, Chutima Boonthum-Denecke</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Artificial Intelligence (AI) and automation has been one of
the most popular topics of the century. It has been
integrated into education, medicine, and transportation to
make tasks easier and increase productivity. AI and
automation is constantly being discussed for being a double
edged sword. On one side, it makes tasks capable of being
completed faster and oftentimes more accurate, but the
other side argues that it lacks accountability. Before AI
and automation is introduced to a system , it is integral
to analyze the pros and cons of said implementation. This
research focuses on the integration of AI and automation in
sports and how its risks can affect athlete data, match
outcomes, and device reliability. Past research has
examined accuracy and health benefits; however, device
security, data flow, and contingency planning in the event
of an attack or breach has not been acknowledged. This
study investigates these gaps by examining how AI-driven
wearables and automated officiating systems function; how
data flow is mapped; and what vulnerabilities affect
confidentiality, integrity, and availability. Literature
reviews and input from sports management and computer
science professionals, athletes, and trainers will
illustrate what protections are currently available and
what they think of the trade-offs. The results will
highlight key risks, identify potential solutions, and
offer guidance for sports organizations and tech developers
so that AI and automation in sports can be both innovative
and secure.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="social media misinformation: trust, perception, &amp; public awareness in the age of ai kayla council, jean muhammad, chutima boonthum-denecke misinformation that spreads through social media platforms is becoming very important since artificial intelligence (ai) is helping the spread of misinformation. a lot of misinformation spreads through manipulated social media posts, and this can cause people to reduce their trust in what they see online, and some people may even be easily persuaded and believe what they see in these manipulated posts. since artificial intelligence is growing and becoming the newest big thing, it’s being used to create posts that are manipulated, and this makes it hard for people to distinguish between real and manipulated posts. this research will analyze how well people can assess social media posts and what factors play a role in their ability to determine what posts are real from the ones that are manipulated. a survey was conducted where people had the opportunity to choose what post they believe is manipulated, and then they were asked what made them choose that choice, and then they rated their confidence level. after gathering all of the results from the survey, the results will be compared with tools that are already created for being able to detect misinformation that’s generated by ai. comparing the human results from the survey with the detection tools will help determine if humans’ ability to spot misinformation is just as good as the detection tools. this research will highlight the difficulties of spotting misinformation in ai-manipulated posts, and it will also show how the cybersecurity side of things can help people continue to trust what they see online with the help of detection tools. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_5.pdf">Social Media Misinformation: Trust, Perception, &amp; Public
Awareness in the Age of AI</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Kayla Council, Jean Muhammad, Chutima Boonthum-Denecke</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Misinformation that spreads through social media platforms
is becoming very important since artificial intelligence
(AI) is helping the spread of misinformation. A lot of
misinformation spreads through manipulated social media
posts, and this can cause people to reduce their trust in
what they see online, and some people may even be easily
persuaded and believe what they see in these manipulated
posts.  Since artificial intelligence is growing and
becoming the newest big thing, it’s being used to create
posts that are manipulated, and this makes it hard for
people to distinguish between real and manipulated posts.
This research will analyze how well people can assess
social media posts and what factors play a role in their
ability to determine what posts are real from the ones that
are manipulated. A survey was conducted where people had
the opportunity to choose what post they believe is
manipulated, and then they were asked what made them choose
that choice, and then they rated their confidence level.
After gathering all of the results from the survey, the
results will be compared with tools that are already
created for being able to detect misinformation that’s
generated by AI. Comparing the human results from the
survey with the detection tools will help determine if
humans’ ability to spot misinformation is just as good as
the detection tools. This research will highlight the
difficulties of spotting misinformation in AI-manipulated
posts, and it will also show how the cybersecurity side of
things can help people continue to trust what they see
online with the help of detection tools.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="the immersive campus experience: designing interactive physical-digital systems for recruitment and ux research morgan bennett, rahnie riggins, karina liles as student recruitment environments become increasingly competitive, institutions must explore innovative, data-driven approaches that integrate experiential design with empirical research. the immersive campus experience is a computer science–led interactive system that reimagines an elevator as a design-simulated university campus using vinyl environmental, qr-code–based interaction, and mobile gameplay mechanics. participants initiate the experience by scanning a qr code that launches a structured, question-driven game in which users navigate campus locations by selecting visual symbols representing academic buildings, student resources, and campus landmarks. beyond recruitment, this project functions as a user experience (ux) research platform. quantitative metrics—including navigation pathways, time spent per decision point, completion rates, replay behavior, and exit points—are collected to evaluate engagement and usability. these metrics allow the team to analyze how users explore the experience, where they disengage, and which campus elements attract the most interest. the collected data informs iterative design improvements while demonstrating practical applications of computer science concepts such as human-computer interaction, data analytics, and interactive system design. the immersive campus experience highlights how physical spaces augmented with digital interactivity can be leveraged for experiential learning, recruitment, and applied research. this project showcases a scalable, low-barrier approach to merging design, technology, and data-driven decision-making, while positioning computer science as both innovative and accessible to prospective students. full-oral student - undergraduate full-oral">
  <h4>The Immersive Campus Experience: Designing Interactive
Physical-Digital Systems for Recruitment and UX Research</h4>
  <div class="paper-meta"><strong>Authors:</strong> Morgan Bennett, Rahnie Riggins, Karina Liles</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">As student recruitment environments become increasingly
competitive, institutions must explore innovative,
data-driven approaches that integrate experiential design
with empirical research. The Immersive Campus Experience is
a computer science–led interactive system that reimagines
an elevator as a design-simulated university campus using
vinyl environmental, QR-code–based interaction, and mobile
gameplay mechanics. Participants initiate the experience by
scanning a QR code that launches a structured,
question-driven game in which users navigate campus
locations by selecting visual symbols representing academic
buildings, student resources, and campus landmarks.
Beyond recruitment, this project functions as a user
experience (UX) research platform. Quantitative
metrics—including navigation pathways, time spent per
decision point, completion rates, replay behavior, and exit
points—are collected to evaluate engagement and usability.
These metrics allow the team to analyze how users explore
the experience, where they disengage, and which campus
elements attract the most interest. The collected data
informs iterative design improvements while demonstrating
practical applications of computer science concepts such as
human-computer interaction, data analytics, and interactive
system design.
The Immersive Campus Experience highlights how physical
spaces augmented with digital interactivity can be
leveraged for experiential learning, recruitment, and
applied research. This project showcases a scalable,
low-barrier approach to merging design, technology, and
data-driven decision-making, while positioning computer
science as both innovative and accessible to prospective
students.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="adversarial patch: autonomous vehicles erick constant, chutima boonthum-denecke when it comes to the safety of autonomous vehicles using computer vision, we must first analysis the impact and risk that adversarial patches may present to its occupants, other drivers and property on the road. by seeing the result of the patch with the ultralytics yolo 11 model trained on things that an autonomous vehicle might encounter on the road we can perform an analysis of what could’ve been the impact without needing to run a simulation. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_9.pdf">Adversarial Patch: Autonomous Vehicles</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Erick Constant, Chutima Boonthum-Denecke</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">When it comes to the safety of autonomous vehicles using
computer vision, we must first analysis the impact and risk
that adversarial patches may present to its occupants,
other drivers and property on the road. By seeing the
result of the patch with the Ultralytics YOLO 11 model
trained on things that an autonomous vehicle might
encounter on the road we can perform an analysis of what
could’ve been the impact without needing to run a
simulation.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="beyond the box score: how analytics shape modern basketball eddie hopkins, kemauri joseph, caleb akintayo, paige felder, karina liles statistical analysis in the modern era of basketball is a vital part of the decision-making process for both individual players and the team as a whole. this research investigates how basketball statistics are gathered, interpreted, and how essential the application of this information is to the improvement of the team and, ultimately, its long-term success. traditional statistics, such as points, assists, rebounds, and turnovers, provide rudimentary insights into a player’s potency and the team’s overall efficiency throughout a game. additionally, advanced statistics that delve deeper into player and team production, such as true shooting percentage(ts%), offensive or defensive rating(ortg/drtg), and points per possession(ppp), help provide deeper evaluations of performances by accounting for overall shooting skill, game pace, and overall team efficiency. with the analysis of these statistics, coaches can easily find the gaps within the team, pinpoint strengths and weaknesses, develop offensive and defensive strategies, enhance lineups, and make additional adjustments needed to help the team thrive against specific opponents. statistical analysis also aids in the development of players, which spotlights areas for improvement as well as predicting a player’s production in future games. the use of statistical analysis promotes strategy, allowing teams to create game plans that improve efficiency, productivity, and ultimately the success of the team overall. full-oral student - undergraduate full-oral">
  <h4>Beyond the Box Score: How Analytics Shape Modern Basketball</h4>
  <div class="paper-meta"><strong>Authors:</strong> Eddie Hopkins, Kemauri Joseph, Caleb Akintayo, Paige Felder, Karina Liles</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Statistical analysis in the modern era of basketball is a
vital part of the decision-making process for both
individual players and the team as a whole. This research
investigates how basketball statistics are gathered,
interpreted, and how essential the application of this
information is to the improvement of the team and,
ultimately, its long-term success. Traditional statistics,
such as points, assists, rebounds, and turnovers, provide
rudimentary insights into a player’s potency and the team’s
overall efficiency throughout a game. Additionally,
advanced statistics that delve deeper into player and team
production, such as true shooting percentage(TS%),
offensive or defensive rating(ORTG/DRTG), and points per
possession(PPP), help provide deeper evaluations of
performances by accounting for overall shooting skill, game
pace, and overall team efficiency. With the analysis of
these statistics, coaches can easily find the gaps within
the team, pinpoint strengths and weaknesses, develop
offensive and defensive strategies, enhance lineups, and
make additional adjustments needed to help the team thrive
against specific opponents. Statistical analysis also aids
in the development of players, which spotlights areas for
improvement as well as predicting a player’s production in
future games. The use of statistical analysis promotes
strategy, allowing teams to create game plans that improve
efficiency, productivity, and ultimately the success of the
team overall.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="an accuracy comparison of linear and quadratic programming approaches for classifying breast cancer cells as malignant or benign jayques nelson, wei wan, yuanyuan peng data classification is a foundational methodology for organizing and labeling data into discrete categories based on predefined criteria and is widely applied across numerous scientific and industrial domains. one of the most interpretable classification approaches is binary classification using a linear separator in a two-dimensional feature space. although conceptually simple, the development of accurate and generalizable linear classification models has been the subject of extensive research. both linear programming (lp) and quadratic programming (qp) formulations have been rigorously established as supervised learning methods for linear classification. this thesis presents a comparative evaluation of these two optimization-based models, focusing on their relative classification performance. using a biomedical dataset for binary diagnostic classification—specifically, the discrimination between malignant and benign breast cancer cells—this study investigates which optimization framework yields superior predictive accuracy. full-oral student - undergraduate full-oral">
  <h4>An Accuracy Comparison of Linear and Quadratic Programming
Approaches for Classifying Breast Cancer Cells as Malignant
or Benign</h4>
  <div class="paper-meta"><strong>Authors:</strong> Jayques Nelson, Wei Wan, Yuanyuan Peng</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Data classification is a foundational methodology for
organizing and labeling data into discrete categories based
on predefined criteria and is widely applied across
numerous scientific and industrial domains. One of the most
interpretable classification approaches is binary
classification using a linear separator in a
two-dimensional feature space. Although conceptually
simple, the development of accurate and generalizable
linear classification models has been the subject of
extensive research. Both linear programming (LP) and
quadratic programming (QP) formulations have been
rigorously established as supervised learning methods for
linear classification. This thesis presents a comparative
evaluation of these two optimization-based models, focusing
on their relative classification performance. Using a
biomedical dataset for binary diagnostic
classification—specifically, the discrimination between
malignant and benign breast cancer cells—this study
investigates which optimization framework yields superior
predictive accuracy.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="gradpath - academic advising platform arqawan noori the undergraduate computer science academic plan is often very complex, represented by a dense prerequisite structure, limited course availability, and an absence of intuitive tools that allow students to visualize their progress against degree requirements. gradpath is a full-stack academic advising platform designed to meet the challenge of academic planning in computer science, giving students and faculty an intuitive, data-driven way to map the student&#x27;s pathway through their degree. this project extends an existing client-side prototype into a scalable, secure, and professionally engineered web application. the system integrates a node.js backend with a postgresql database that houses student records, degree requirements, semester schedules, and utilizes jwt-based authentication for secure access. on the frontend, an enhanced react interface offers dynamic degree visualization, cross-semester prerequisite validation, and intelligent course-recommendation algorithms that adapt based on each student&#x27;s completed credits and official academic map. additional features include an advisor dashboard to review and approve student plans, a comprehensive testing suite using jest and react testing library, and a continuous integration/continuous deployment pipeline for automated deployment. gradpath showcases how modern software engineering can be effectively utilized to empower better academic decision-making while reducing the bottlenecks that often impede the advising process and hinder students&#x27; success in complex degree programs. full-oral student - undergraduate full-oral">
  <h4>Gradpath - Academic Advising platform</h4>
  <div class="paper-meta"><strong>Authors:</strong> Arqawan Noori</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The undergraduate computer science academic plan is often
very complex, represented by a dense prerequisite
structure, limited course availability, and an absence of
intuitive tools that allow students to visualize their
progress against degree requirements. GradPath is a
full-stack academic advising platform designed to meet the
challenge of academic planning in computer science, giving
students and faculty an intuitive, data-driven way to map
the student&#x27;s pathway through their degree. This project
extends an existing client-side prototype into a scalable,
secure, and professionally engineered web application. The
system integrates a Node.js backend with a PostgreSQL
database that houses student records, degree requirements,
semester schedules, and utilizes JWT-based authentication
for secure access. On the frontend, an enhanced React
interface offers dynamic degree visualization,
cross-semester prerequisite validation, and intelligent
course-recommendation algorithms that adapt based on each
student&#x27;s completed credits and official academic map.
Additional features include an advisor dashboard to review
and approve student plans, a comprehensive testing suite
using Jest and React Testing Library, and a continuous
integration/continuous deployment pipeline for automated
deployment. GradPath showcases how modern software
engineering can be effectively utilized to empower better
academic decision-making while reducing the bottlenecks
that often impede the advising process and hinder students&#x27;
success in complex degree programs.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="robots for outreach zora stephens, karina liles using claflin university’s robots, we will program them to support our outreach efforts in computer science. the goal is to engage potential students and visitors with our computer science department through interactive demonstrations. a series of programs has been developed to illustrate the importance and diversity of computer science using the nao humanoid and unitree go2 robots. these activities aim to instill basic computer science principles such as sequencing, conditional statements, sensor-based decision-making, and human-robot interaction. during outreach events, the robots perform demonstrations to help participants see how code translates into physical actions, demystifying programming, and robotics. by providing an interactive and visually engaging experience, computer science can be made more accessible to individuals with varying levels of technical background. this project demonstrates how robotics can be an effective tool for computer science outreach, increasing engagement, encouraging curiosity, and fostering interest in computing disciplines. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_22.pdf">Robots for Outreach</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Zora Stephens, Karina Liles</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Using Claflin University’s robots, we will program them to
support our outreach efforts in computer science. The goal
is to engage potential students and visitors with our
computer science department through interactive
demonstrations. A series of programs has been developed to
illustrate the importance and diversity of computer science
using the NAO humanoid and Unitree Go2 robots. These
activities aim to instill basic computer science principles
such as sequencing, conditional statements, sensor-based
decision-making, and human-robot interaction. During
outreach events, the robots perform demonstrations to help
participants see how code translates into physical actions,
demystifying programming, and robotics. By providing an
interactive and visually engaging experience, computer
science can be made more accessible to individuals with
varying levels of technical background. This project
demonstrates how robotics can be an effective tool for
computer science outreach, increasing engagement,
encouraging curiosity, and fostering interest in computing
disciplines.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="enabling safe beyond visual line of sight drone operations of sight drone operations through ai-powered object detection aniya hopson, chutima boonthum-denecke as artificial intelligence (ai) becomes a powerful force within the technological field it is being integrated into all fields. as ai improves, optimizing it for everyday life is beneficial for the further development of technology. in this paper, we present our research findings and literature on adversarial examples and object detection. this research builds upon the previous work by investigating and optimizing an unmanned aircraft to be flown with the aid of artificial intelligence. we started with classifying and training ai to recognize certain objects on yolov11 custom trained models. then a follow-up using the custom trained model with live drone footage to test the accuracy of the model evaluating how it can be utilized in beyond visual line of sight (bvlos). through this exploration it demonstrates the future of using unmanned aircrafts with support from machine learning. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_28.pdf">Enabling safe Beyond Visual Line of Sight Drone Operations
of Sight Drone Operations Through AI-Powered Object
Detection</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Aniya Hopson, Chutima Boonthum-Denecke</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">As Artificial Intelligence (AI) becomes a powerful force
within the technological field it is being integrated into
all fields. As AI improves, optimizing it for everyday life
is beneficial for the further development of technology. In
this paper, we present our research findings and literature
on adversarial examples and object detection. This research
builds upon the previous work by investigating and
optimizing an unmanned aircraft to be flown with the aid of
Artificial Intelligence. We started with classifying and
training AI to recognize certain objects on YOLOv11 custom
trained models. Then a follow-up using the custom trained
model with live drone footage to test the accuracy of the
model evaluating how it can be utilized in Beyond Visual
Line of Sight (BVLOS). Through this exploration it
demonstrates the future of using unmanned aircrafts with
support from machine learning.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="budget aware tracerouting bakri diyaolu, adin lindsey, jeremiah adderley traditional traceroute tools send a fixed number of probes per hop, leading to redundant measurements and inefficient use of network resources. this research introduces a budget-aware traceroute system (bat) designed to optimize probing efficiency while preserving accurate path discovery. using scamper as the probing engine, bat dynamically allocates probe “credits” across hops based on per-hop confidence levels. this work highlights the potential for adaptive network measurement systems that balance precision, responsiveness, and bandwidth efficiency in large-scale internet topology mapping. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_45.pdf">Budget Aware Tracerouting</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Bakri Diyaolu, Adin Lindsey, Jeremiah Adderley</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge"></span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Traditional traceroute tools send a fixed number of probes
per hop, leading to redundant measurements and inefficient
use of network resources. This research introduces a
budget-aware traceroute system (BAT) designed to optimize
probing efficiency while preserving accurate path
discovery. Using Scamper as the probing engine, BAT
dynamically allocates probe “credits” across hops based on
per-hop confidence levels. This work highlights the
potential for adaptive network measurement systems that
balance precision, responsiveness, and bandwidth efficiency
in large-scale Internet topology mapping.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="enhancing black-box transparency with shap and lime: a comparative and practical review of explainable ai in cybersecurity danae ludy, janett walters-williams as machine learning models are increasingly deployed in cybersecurity systems, their black-box nature complicates trust, accountability, and post-incident investigation. explainable artificial intelligence (xai) addresses these challenges by providing human-interpretable insights into model behavior without sacrificing predictive performance. using a standard xai taxonomy, the paper compares shapley additive explanations (shap) and local interpretable model-agonistic explanations (lime) in terms of theoretical grounding, stability, interaction awareness, and operational suitability for forensic analysis and intrusion detection. the discussion highlights governance and deployment considerations and outlines future research directions that integrate complementary visualization techniques to strengthen interpretability in cybersecurity workflows. the findings motivate a complementary use of shap for global oversight and defensible local attribution, with lime applied selectively for rapid case-based analysis. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_55.pdf">Enhancing Black-Box Transparency with SHAP and LIME: A
Comparative and Practical Review of Explainable AI in
Cybersecurity</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Danae Ludy, Janett Walters-Williams</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">REJECT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">As machine learning models are increasingly deployed in
cybersecurity systems, their black-box nature complicates
trust, accountability, and post-incident investigation.
Explainable Artificial Intelligence (XAI) addresses these
challenges by providing human-interpretable insights into
model behavior without sacrificing predictive performance.
Using a standard XAI taxonomy, the paper compares Shapley
Additive Explanations (SHAP) and Local Interpretable
Model-agonistic Explanations (LIME) in terms of theoretical
grounding, stability, interaction awareness, and
operational suitability for forensic analysis and intrusion
detection. The discussion highlights governance and
deployment considerations and outlines future research
directions that integrate complementary visualization
techniques to strengthen interpretability in cybersecurity
workflows. The findings motivate a complementary use of
SHAP for global oversight and defensible local attribution,
with LIME applied selectively for rapid case-based analysis.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="detecting hidden multiprotocol label switching tunnels (mpls) in networks eyimofe ajagunna, blessed kutyauripo, ledarius robinson this research focuses on developing a reliable methodology for detecting hidden mpls (multiprotocol label switching) tunnels using active network probing. our proposed algorithm combines geographic anomalies, rtt behavior, hostname patterns, and backbone routing characteristics to distinguish mpls tunnels from ordinary routing behaviors such as load balancing. furthermore, our detection pipeline is implemented to automate tunnel identification, estimate tunnel boundaries, and visualize hop-level behavior. the purpose of this research is to create an accurate, reproducible framework for uncovering concealed mpls structures in modern networks, enabling improved transparency, routing analysis, and network measurement accuracy. full-oral student - undergraduate full-oral">
  <h4>Detecting Hidden Multiprotocol Label Switching Tunnels
(MPLS) In Networks</h4>
  <div class="paper-meta"><strong>Authors:</strong> Eyimofe Ajagunna, Blessed Kutyauripo, Ledarius Robinson</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge"></span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This research focuses on developing a reliable methodology
for detecting hidden MPLS (Multiprotocol Label Switching)
tunnels using active network probing.
Our proposed algorithm combines geographic anomalies, RTT
behavior, hostname patterns, and backbone routing
characteristics to distinguish MPLS tunnels from ordinary
routing behaviors such as load balancing.
Furthermore, our detection pipeline is implemented to
automate tunnel identification, estimate tunnel boundaries,
and visualize hop-level behavior.
The purpose of this research is to create an accurate,
reproducible framework for uncovering concealed MPLS
structures in modern networks, enabling improved
transparency, routing analysis, and network measurement
accuracy.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="online anonymity vs. online accountability gabrielle olds, jean muhammad the main problem with the conflict between online anonymity and accountability is that, although anonymity promotes privacy and free speech, it also makes harmful behaviors like trolling and scams possible. in order to understand how mandatory identification policies, like requiring government ids or facial scans for site access, affect this balance, this study will review previous research. privacy and security risks will be a major focus because private businesses collect extremely sensitive data, increasing the risk of data breaches, long-term identity theft, and user tracking. in order to make fair policy decisions, a survey will also be carried out to find out how the public feels about these intrusive verification techniques. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_63.pdf">Online Anonymity vs. Online Accountability</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Gabrielle Olds, Jean Muhammad</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The main problem with the conflict between online anonymity
and accountability is that, although anonymity promotes
privacy and free speech, it also makes harmful behaviors
like trolling and scams possible. In order to understand
how mandatory identification policies, like requiring
government IDs or facial scans for site access, affect this
balance, this study will review previous research. Privacy
and security risks will be a major focus because private
businesses collect extremely sensitive data, increasing the
risk of data breaches, long-term identity theft, and user
tracking. In order to make fair policy decisions, a survey
will also be carried out to find out how the public feels
about these intrusive verification techniques.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="feature effect visualization in cybersecurity: a study of pdp and ice clarence bostic, janet williams the integration of artificial intelligence (ai) into cybersecurity has significantly developed advanced threat detection and analysis. however, due to the deep learning nature, the inherent opacity that comes with these “black box” models creates doubts in the decisions of incident investigation. explainable artificial intelligence (xai) is the backbone of the future of this transparency gap, by utilizing visualization tools to make these decisions more interpretable. this paper examines two feature-visualization tools in cybersecurity: partial dependence plots (pdps) and individual conditional ex- pectation (ice) plots. we analyse the differences between pdps, which are global explanations, by averaging the effects, and ice plots, which offer local instance-level insights, to show heteroge- neous attack patterns. by evaluating these methods with the focus of improving cybersecurity intrusion detection and malware anal- ysis. this study highlights the necessary balance between clarity and depth to enhance operational reliability in ai-driven security systems. full-oral student - undergraduate full-oral">
  <h4><a href="sorted_papers/Full-Oral/Student - Undergraduate/ADMI_2026_paper_66.pdf">Feature Effect Visualization in Cybersecurity: A Study of
PDP and ICE</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Clarence Bostic, Janet Williams</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The integration of Artificial Intelligence (AI) into
cybersecurity
has significantly developed advanced threat detection and
analysis.
However, due to the deep learning nature, the inherent
opacity that
comes with these “black box” models creates doubts in the
decisions
of incident investigation. Explainable Artificial
Intelligence (XAI)
is the backbone of the future of this transparency gap, by
utilizing
visualization tools to make these decisions more
interpretable. This
paper examines two feature-visualization tools in
cybersecurity:
Partial Dependence Plots (PDPs) and Individual Conditional
Ex-
pectation (ICE) plots. We analyse the differences between
PDPs,
which are global explanations, by averaging the effects,
and ICE
plots, which offer local instance-level insights, to show
heteroge-
neous attack patterns. By evaluating these methods with the
focus
of improving cybersecurity intrusion detection and malware
anal-
ysis. This study highlights the necessary balance between
clarity
and depth to enhance operational reliability in AI-driven
security
systems.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Full-Oral" data-authorcat="Student - Undergraduate" data-search="digitizing textbook adoption processes: a role-based web system for academic workflow optimization shovkat zeynalli this paper presents the design and implementation of a web-based textbook adoption management system developed to improve the efficiency and transparency of textbook ordering processes within a university setting. traditional textbook adoption procedures often rely on manual paperwork and email communication, which can result in delays, miscommunication, and limited visibility across departments. the proposed system introduces a role-based workflow that enables instructors to submit textbook adoption forms electronically, allows heads of departments (hods) to review and approve submissions, and provides bookstore personnel with access to finalized textbook orders. the application was developed using a react frontend, a node.js and express backend, and a mysql relational database to ensure structured data management and scalability. key features include secure authentication, role-based access control, dynamic form handling, and persistent database storage. the system demonstrates how modern web technologies can be applied to streamline administrative processes in higher education while improving accountability and operational efficiency. full-oral student - undergraduate full-oral">
  <h4>Digitizing Textbook Adoption Processes: A Role-Based Web
System for Academic Workflow Optimization</h4>
  <div class="paper-meta"><strong>Authors:</strong> Shovkat Zeynalli</div>
  <div class="paper-meta"><strong>Submission type:</strong> Full-Oral</div>
  <div class="badges">
    <span class="badge fulloral">Full-Oral</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Full-Oral</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This paper presents the design and implementation of a
web-based Textbook Adoption Management System developed to
improve the efficiency and transparency of textbook
ordering processes within a university setting. Traditional
textbook adoption procedures often rely on manual paperwork
and email communication, which can result in delays,
miscommunication, and limited visibility across
departments. The proposed system introduces a role-based
workflow that enables instructors to submit textbook
adoption forms electronically, allows Heads of Departments
(HoDs) to review and approve submissions, and provides
bookstore personnel with access to finalized textbook
orders. The application was developed using a React
frontend, a Node.js and Express backend, and a MySQL
relational database to ensure structured data management
and scalability. Key features include secure
authentication, role-based access control, dynamic form
handling, and persistent database storage. The system
demonstrates how modern web technologies can be applied to
streamline administrative processes in higher education
while improving accountability and operational efficiency.</div>
  </details>
</article>

</div>
</div>

</div>

<div class="section-block section-anchor" id="posters">

## Posters


<p class="small-note">47 submissions in this section.</p>

<div class="category-block section-anchor" id="poster-student-graduate">

### Student - Graduate


<p class="category-meta">1 submissions</p>

<div class="paper-list">

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Graduate" data-search="addressing fairness and trustworthiness in the workplace using scalable blockchain survey solutions hamid kabia, blayne montaque, saurav aryal fairness and trustworthiness are principles that were implemented into the workplace to allow for the growth of a more competitive career marketplace in which all individuals have equal opportunity at a role regardless of external matters such as race, religion, gender, or sexuality [1]. however, despite the positive impacts these initiatives have had in the work place, in recent years there&#x27;s been a push back against them. with multiple organizations even going as far as rolling back their programs supporting fairness in the workplace. to combat this we have developed a tool that allows for anonymous insider reporting of a company’s policies through the blockchain. through the use of this tool we hope to allow consumers and potential jobseekers to make informed decisions about the companies they patronize. poster student - graduate poster">
  <h4><a href="sorted_papers/Poster/Student - Graduate/ADMI_2026_paper_57.pdf">Addressing Fairness and Trustworthiness in The Workplace
Using Scalable Blockchain Survey Solutions</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Hamid Kabia, Blayne Montaque, Saurav Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Graduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Fairness and trustworthiness are principles that were
implemented into the workplace to allow for the growth of a
more competitive career marketplace in which all
individuals have equal opportunity at a role regardless of
external matters such as race, religion, gender, or
sexuality [1]. However, despite the positive impacts these
initiatives have had in the work place, in recent years
there&#x27;s been a push back against them. With multiple
organizations even going as far as rolling back their
programs supporting fairness in the workplace. To combat
this we have developed a tool that allows for anonymous
insider reporting of a company’s policies through the
blockchain. Through the use of this tool we hope to allow
consumers and potential jobseekers to make informed
decisions about the companies they patronize.</div>
  </details>
</article>

</div>
</div>

<div class="category-block section-anchor" id="poster-student-undergraduate">

### Student - Undergraduate


<p class="category-meta">55 submissions</p>

<div class="paper-list">

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="machine learning diagnosis of peripheral arterial disease from ct-angiography (cta) images amrinder singh, caliese beckford, subash neupane, demi ashade, swikriti neupane, bimal itani, verlie tisdale, shrikant pawar introduction: peripheral arterial disease (pad) is a common circulatory problem characterized by narrowed arteries that reduce blood flow to the lower extremities. in 2019 the global burden of disease study attributed over 74,000 deaths to pad with over 113,000,000 individuals living with the condition globally. despite its prevalence, accurate and timely diagnosis remains a challenge, often leading to severe complications such as muscular weakness, amputation etc. study objectives: this research investigates the use of machine learning specifically convolutional neural networks (cnns), to enhance pad diagnosis from ct-angiography (cta) images. methods: the study aims to determine the effectiveness of neural networks in detecting pad, optimize model performance, and deploy a testing application for clinical use. we have generated pad ml model by utilizing pretrained resnet-50 architecture on pytorch framework with dataset splits of 80% training and 20% validation, a adamw optimizer for 500 epochs. results: overall, the model shows stable validation performance with high accuracy, f1-score, and auc. metrics remain consistent in later epochs, and the selected checkpoint reflects strong generalization behavior. a validation accuracy of ~93–94%, precision of ~0.93–0.95, recall of ~0.91–0.94, f1-score of ~0.93, and an auc of ~0.97–0.98 was observed from training (figure 1). discussion: by improving diagnostic accuracy, this project has the potential to facilitate early detection and treatment of pad, reducing the risk of severe outcomes. the integration of machine learning models into clinical workflows represents a significant step toward more accessible and efficient pad diagnostics, ultimately improving patient care and outcomes. figure 1: validation area under the curve (auc) for detecting pad. acknowledgment: this study is funded by national science foundation south carolina established program for stem cooperative research (sc epscor), ai-enabled devices for the advancement of personalized and transformative healthcare in south carolina adapt, rii track-1, award number: 2242812, claflin university sub-awardees tisdale verlie and pawar shrikant. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_2.pdf">Machine Learning Diagnosis of Peripheral Arterial Disease
from CT-Angiography (CTA) Images</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Amrinder Singh, Caliese Beckford, Subash Neupane, Demi Ashade, Swikriti Neupane, Bimal Itani, Verlie Tisdale, Shrikant Pawar</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Introduction: Peripheral Arterial Disease (PAD) is a common
circulatory problem characterized by narrowed arteries that
reduce blood flow to the lower extremities. In 2019 the
global burden of disease study attributed over 74,000
deaths to PAD with over 113,000,000 individuals living with
the condition globally. Despite its prevalence, accurate
and timely diagnosis remains a challenge, often leading to
severe complications such as muscular weakness, amputation
etc.

Study Objectives: This research investigates the use of
machine learning specifically Convolutional Neural Networks
(CNNs), to enhance PAD diagnosis from CT-Angiography (CTA)
images.

Methods: The study aims to determine the effectiveness of
neural networks in detecting PAD, optimize model
performance, and deploy a testing application for clinical
use. We have generated PAD ML model by utilizing pretrained
ResNet-50 architecture on PyTorch Framework with dataset
splits of 80% training and 20% validation, a AdamW
optimizer for 500 epochs.

Results:  Overall, the model shows stable validation
performance with high accuracy, F1-score, and AUC. Metrics
remain consistent in later epochs, and the selected
checkpoint reflects strong generalization behavior.  A
validation accuracy of ~93–94%, precision of ~0.93–0.95,
recall of ~0.91–0.94, F1-score of ~0.93, and an AUC of
~0.97–0.98 was observed from training (Figure 1).

Discussion: By improving diagnostic accuracy, this project
has the potential to facilitate early detection and
treatment of PAD, reducing the risk of severe outcomes. The
integration of machine learning models into clinical
workflows represents a significant step toward more
accessible and efficient PAD diagnostics, ultimately
improving patient care and outcomes.

Figure 1: Validation Area Under the Curve (AUC) for
detecting PAD.

Acknowledgment: This study is funded by National Science
Foundation South Carolina Established Program for Stem
Cooperative Research (SC EPSCoR), AI-enabled Devices for
the Advancement of Personalized and Transformative
Healthcare in South Carolina ADAPT, RII Track-1, Award
Number: 2242812, Claflin University Sub-awardees Tisdale
Verlie and Pawar Shrikant.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="ai-enabled construction of aligned collagen using two-photon techniques caliese beckford, wesley nicolas, zhi gao, shrikant pawar introduction: laser-based collagen biofabrication process is a novel approach for generating customizable 3d collagen structures as an in-vitro tissue scaffold and has the potential for in-vivo tissue engineering. the technology stems from the ability of a femtosecond (fs) laser pulse to optically generate a controlled and localized ph gradient via a two photon (2p) effect that facilitates the generation of collagen protein assembly, called fibrillogenesis, into fibers and bundles. unlike all other collagen biofabrication techniques, this process utilizes the spatial and temporal precision attributed to light, which allows for accurate 3d modeling of native tissue structure. tseng et. al, 2020 proposed a framework for a functional biopolymer that could alternate between the two β-sheet structures in response to ph changes. chiba et. al, 2003 have extensively studied amyloidogenicity showing a significant correlation with the stability of the amyloid fibrils with ph, and little correlation with that of the native state. it has been proposed that the stability of the native state and the unfolding rate to the amyloidogenic precursor as well as the conformational preference of the denatured state is influenced by ph. the most immediate impact of collagen fabrication would be in the creation of custom, patterned cell culture scaffolds. here, we propose an ai based innovative laser collagen alignment technique to be developed into an in-situ scaffold formation technology for producing next generation of tissue engineering-based implantable biomedical devices. study objectives: this research investigates if the use of trained convolutional neural net architecture (cnn) can effectively segment aligned collagen fibers deep inside tissue, this study set out to train a u-net cnn architecture to accurately classify aligned collagen-positive pixels within a shg image volume. this ai-enabled collagen image processing opens a new way to create real-time scaffold formation technique that mimic various in vivo tissue structures. methods: to achieve this, we have used pytorch, a python library to initialize the conventional u-net cnn with four encoding and decoding units on 2000 images (figure 1). the synthetic images were generated utilizing a stable diffusion 3.5 large technique. a non-linear rectified non-linear unit (relu) layer comes after two 2d convolution layers in each encoding and decoding block. the network&#x27;s weights and biases are modified by an adaptive moment (adam) optimizer. these findings will assess whether a trained cnn can accurately and precisely segment aligned collagen-positive pixels at a variety of imaging depths assisting our understanding of fibrillogenesis and subsequently collagen biofabrication. results: primary training found the model to have a training loss of 0.009 with a precision and recall of &gt; 0.90. however, an overfitting has been observed with this run. to fix this, we intend to increase data (via augmentation), simplify the model by having fewer layers, try regularization (l1/l2), implement early stopping, or will apply k-fold cross-validation to improve generalization. as an alternative, transfer learning can be used to modify the trained cnn for use in drastically distinct fiber networks or to retrain the network for images at significantly different magnifications. discussion: here, we propose an ai based innovative laser collagen alignment technique to be developed into an in-situ scaffold formation technology for producing next generation of tissue engineering-based implantable biomedical devices. this ai-enabled collagen image processing opens a new way to create real-time scaffold formation technique that mimic various in vivo tissue structure. these findings will assess whether a trained cnn can more accurately and precisely segment aligned collagen-positive pixels at a variety of imaging depths. figure 1: sample image for aligned and un-aligned collagen fibrils used in cnn training. acknowledgment: this study is funded by national science foundation south carolina established program for stem cooperative research (sc epscor), gain crp subaward (grants for applications in industry and networking collaborative research program), claflin university sub-awardee pawar shrikant. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_3.pdf">AI-Enabled Construction of Aligned Collagen Using
Two-Photon Techniques</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Caliese Beckford, Wesley Nicolas, Zhi Gao, Shrikant Pawar</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Introduction: Laser-based collagen biofabrication process
is a novel approach for generating customizable 3D collagen
structures as an in-vitro tissue scaffold and has the
potential for in-vivo tissue engineering. The technology
stems from the ability of a femtosecond (fs) laser pulse to
optically generate a controlled and localized pH gradient
via a two photon (2P) effect that facilitates the
generation of collagen protein assembly, called
fibrillogenesis, into fibers and bundles. Unlike all other
collagen biofabrication techniques, this process utilizes
the spatial and temporal precision attributed to light,
which allows for accurate 3D modeling of native tissue
structure. Tseng et. al, 2020 proposed a framework for a
functional biopolymer that could alternate between the two
β-sheet structures in response to pH changes. Chiba et. al,
2003 have extensively studied amyloidogenicity showing a
significant correlation with the stability of the amyloid
fibrils with PH, and little correlation with that of the
native state. It has been proposed that the stability of
the native state and the unfolding rate to the
amyloidogenic precursor as well as the conformational
preference of the denatured state is influenced by PH. The
most immediate impact of collagen fabrication would be in
the creation of custom, patterned cell culture scaffolds.
Here, we propose an AI based innovative laser collagen
alignment technique to be developed into an in-situ
scaffold formation technology for producing next generation
of tissue engineering-based implantable biomedical devices.

Study Objectives: This research investigates if the use of
trained convolutional neural net architecture (CNN) can
effectively segment aligned collagen fibers deep inside
tissue, this study set out to train a U-Net CNN
architecture to accurately classify aligned
collagen-positive pixels within a SHG image volume.  This
AI-enabled collagen image processing opens a new way to
create real-time scaffold formation technique that mimic
various in vivo tissue structures.

Methods: To achieve this, we have used PyTorch, a python
library to initialize the conventional U-Net CNN with four
encoding and decoding units on 2000 images (Figure 1). The
synthetic images were generated utilizing a Stable
Diffusion 3.5 Large technique. A non-linear rectified
non-linear unit (ReLU) layer comes after two 2D convolution
layers in each encoding and decoding block. The network&#x27;s
weights and biases are modified by an adaptive moment
(ADAM) optimizer. These findings will assess whether a
trained CNN can accurately and precisely segment aligned
collagen-positive pixels at a variety of imaging depths
assisting our understanding of fibrillogenesis and
subsequently collagen biofabrication.

Results:  Primary training found the model to have a
training loss of 0.009 with a precision and recall of &gt;
0.90. However, an overfitting has been observed with this
run. To fix this, we intend to increase data (via
augmentation), simplify the model by having fewer layers,
try regularization (L1/L2), implement early stopping, or
will apply K-Fold cross-validation to improve
generalization. As an alternative, transfer learning can be
used to modify the trained CNN for use in drastically
distinct fiber networks or to retrain the network for
images at significantly different magnifications.

Discussion: Here, we propose an AI based innovative laser
collagen alignment technique to be developed into an
in-situ scaffold formation technology for producing next
generation of tissue engineering-based implantable
biomedical devices. This AI-enabled collagen image
processing opens a new way to create real-time scaffold
formation technique that mimic various in vivo tissue
structure. These findings will assess whether a trained CNN
can more accurately and precisely segment aligned
collagen-positive pixels at a variety of imaging depths.

Figure 1: Sample image for aligned and un-aligned collagen
fibrils used in CNN training.

Acknowledgment: This study is funded by National Science
Foundation South Carolina Established Program for Stem
Cooperative Research (SC EPSCoR), GAIN CRP Subaward (Grants
for Applications in Industry and Networking Collaborative
Research Program), Claflin University Sub-awardee Pawar
Shrikant.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="peerconnect: optimizing peer tutoring with predictive analytics and intelligent matching teniola oluwaseyitan abstract peerconnect is an advanced mobile application designed to enhance academic support and peer-led learning by connecting students with compatible tutors based on their strengths, learning needs, and performance data. addressing the challenges students face in finding effective academic assistance, the platform leverages predictive analytics and intelligent matching algorithms to recommend the most suitable tutors, optimize session scheduling, and monitor student progress, creating a personalized and data-driven learning experience. the application incorporates features such as user registration, detailed tutor profiles with performance statistics, progress tracking dashboards, session scheduling with conflict detection, and ai-driven recommendations for study materials and tutors. built as an ios application using swift with a python-powered backend and mysql database, peerconnect prioritizes accessibility, user experience, and responsive design, making it suitable for students across diverse academic disciplines. by integrating mathematical concepts such as weighted scoring, regression analysis, graph-based network modeling, and predictive probability, peerconnect not only strengthens the peer tutoring process but also provides measurable insights into student performance and learning outcomes. the platform fosters a culture of collaborative learning, academic improvement, and knowledge sharing, offering a structured, reliable, and scalable alternative to informal or traditional tutoring services. peerconnect ultimately aims to enhance student academic performance, engagement, and retention by providing a robust, technology-driven peer support system. future development may expand ai-driven analytics, subject coverage, and integration with institutional learning management systems, highlighting the transformative potential of math-informed, data-driven educational technology in higher education poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_11.pdf">PeerConnect: Optimizing Peer Tutoring with Predictive
Analytics and  Intelligent Matching</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Teniola Oluwaseyitan</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Abstract
PeerConnect is an advanced mobile application designed to
enhance academic support and peer-led learning by
connecting students with compatible tutors based on their
strengths, learning needs, and performance data. Addressing
the challenges students face in finding effective academic
assistance, the platform leverages predictive analytics and
intelligent matching algorithms to recommend the most
suitable tutors, optimize session scheduling, and monitor
student progress, creating a personalized and data-driven
learning experience.
The application incorporates features such as user
registration, detailed tutor profiles with performance
statistics, progress tracking dashboards, session
scheduling with conflict detection, and AI-driven
recommendations for study materials and tutors. Built as an
iOS application using Swift with a Python-powered backend
and MySQL database, PeerConnect prioritizes accessibility,
user experience, and responsive design, making it suitable
for students across
diverse academic disciplines.
By integrating mathematical concepts such as weighted
scoring, regression analysis, graph-based network modeling,
and predictive probability, PeerConnect not only
strengthens the peer tutoring process but also provides
measurable insights into student performance and learning
outcomes. The platform fosters a culture of collaborative
learning, academic improvement, and knowledge sharing,
offering a structured, reliable, and scalable alternative
to informal or traditional tutoring
services.
PeerConnect ultimately aims to enhance student academic
performance, engagement, and
retention by providing a robust, technology-driven peer
support system. Future development may expand AI-driven
analytics, subject coverage, and integration with
institutional learning management systems, highlighting the
transformative potential of math-informed, data-driven
educational technology in higher education</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="deep learning in network traffic analysis using synthetic data for privacy protection and cyber attack mitigation swikriti neupane, pratap sahu intrusion detection systems (ids) are important for identifying malicious network activity, but they rely heavily on large, labeled datasets for effective training. a major challenge in this field is that real network data often contains personally identifiable information (pii), such as ip addresses and hostnames, creating significant privacy and security risks. this research aims to develop a pipeline that removes pii from network datasets while maintaining their research utility. the objective is to generate high-quality synthetic datasets that enable secure data sharing for ids without compromising sensitive information. the study utilized the cic-ids-2017 dataset to reflect authentic network activity and diverse cyberattack types. the methodology involved a multi-stage process: first, pii detection was performed using pattern-matching for ips, mac addresses, and urls. this was followed by anonymization through tokenization (e.g., replacing ips with coded labels) and generalization (e.g., converting specific timestamps to dates). finally, synthetic data was generated using conditional generative adversarial networks (ctgan). the primary goal was to create synthetic records that mimic the statistical distributions of the original traffic without exposing individual identities. the effectiveness of the synthetic data was evaluated across three dimensions: utility, diversity, and privacy. in terms of utility, machine learning models trained on synthetic data achieved significant performance improvement compared to models trained on real data. diversity metrics confirmed that the synthetic datasets maintained consistent label distributions and generated enough unique samples to prevent model overfitting. finally, privacy was validated by measuring the distance between synthetic records and their nearest real samples. the results showed a significant average distance of 23,952,242.9681 and a minimum distance of 2,583,688.0567, indicating that the synthetic records are not direct copies of the original data. these findings suggest that synthetic data generation is a powerful tool for ids research, enabling secure data sharing and mitigation of cyberattacks while ensuring total privacy protection. future work will focus on exploring graph neural networks (gnns), automated end-to-end pipelines, and techniques to ensure fairness across rare attack classes. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_14.pdf">Deep Learning in Network Traffic Analysis Using Synthetic
Data for Privacy Protection and Cyber Attack Mitigation</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Swikriti Neupane, Pratap Sahu</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Intrusion Detection Systems (IDS) are important for
identifying malicious network activity, but they rely
heavily on large, labeled datasets for effective training.
A major challenge in this field is that real network data
often contains Personally Identifiable Information (PII),
such as IP addresses and hostnames, creating significant
privacy and security risks. This research aims to develop a
pipeline that removes PII from network datasets while
maintaining their research utility. The objective is to
generate high-quality synthetic datasets that enable secure
data sharing for IDS without compromising sensitive
information.
The study utilized the CIC-IDS-2017 dataset to reflect
authentic network activity and diverse cyberattack types.
The methodology involved a multi-stage process: first, PII
detection was performed using pattern-matching for IPs, MAC
addresses, and URLs. This was followed by anonymization
through tokenization (e.g., replacing IPs with coded
labels) and generalization (e.g., converting specific
timestamps to dates). Finally, synthetic data was generated
using Conditional Generative Adversarial Networks (CTGAN).
The primary goal was to create synthetic records that mimic
the statistical distributions of the original traffic
without exposing individual identities.
The effectiveness of the synthetic data was evaluated
across three dimensions: Utility, Diversity, and Privacy.
In terms of utility, machine learning models trained on
synthetic data achieved significant performance improvement
compared to models trained on real data. Diversity metrics
confirmed that the synthetic datasets maintained consistent
label distributions and generated enough unique samples to
prevent model overfitting. Finally, privacy was validated
by measuring the distance between synthetic records and
their nearest real samples. The results showed a
significant average distance of 23,952,242.9681 and a
minimum distance of 2,583,688.0567, indicating that the
synthetic records are not direct copies of the original
data. These findings suggest that synthetic data generation
is a powerful tool for IDS research, enabling secure data
sharing and mitigation of cyberattacks while ensuring total
privacy protection. Future work will focus on exploring
Graph Neural Networks (GNNs), automated end-to-end
pipelines, and techniques to ensure fairness across rare
attack classes.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="semantic search for healthcare patient data using sentence transformers and chromadb megan rabb, shani walker, joniqua bates, nikunja swain, biswajit biswal, janmejay mohanty, xiaomao liu healthcare systems often store large volumes of patient records in formats that are difficult to search efficiently using traditional keyword-based methods. these limitations can delay care, frustrate providers, and impact outcomes. a solution is needed that understands the context and meaning behind clinical documentation, enabling faster and more intelligent access to related cases. semantic search is changing the way we manage healthcare information by helping us understand the meaning behind patient records instead of just looking for exact words. in this project, we used google colab to build a simple but powerful semantic search system that combines sentence transformers and chromadb. the goal was to make it easier to find similar patient cases or notes based on meaning. we used a pre-trained transformer model (&quot;all-minilm-l6-v2&quot;) to turn sentences about patient data into numerical vectors. these vectors were saved and searched using chromadb, a lightweight vector database. all coding and testing were done in google colab. for example, when we searched for &quot;high blood pressure treatment,&quot; the system returned a sentence about &quot;medication for hypertension&quot; - proving that it could understand medical terms even if they were worded differently. this kind of system can make it easier for doctors or medical staff to find relevant records quickly, especially in electronic health record systems. overall, this project shows how machine learning tools like sentence embeddings can make healthcare data smarter and more useful. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_15.pdf">Semantic Search for Healthcare Patient Data using Sentence
Transformers and ChromaDB</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Megan Rabb, Shani Walker, Joniqua Bates, Nikunja Swain, Biswajit Biswal, Janmejay Mohanty, Xiaomao Liu</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Healthcare systems often store large volumes of patient
records in formats that are difficult to search efficiently
using traditional keyword-based methods. These limitations
can delay care, frustrate providers, and impact outcomes. A
solution is needed that understands the context and meaning
behind clinical documentation, enabling faster and more
intelligent access to related cases.
Semantic search is changing the way we manage healthcare
information by helping us understand the meaning behind
patient records instead of just looking for exact words. In
this project, we used Google Colab to build a simple but
powerful semantic search system that combines Sentence
Transformers and ChromaDB. The goal was to make it easier
to find similar patient cases or notes based on meaning. We
used a pre-trained transformer model (&quot;all-MiniLM-L6-v2&quot;)
to turn sentences about patient data into numerical
vectors. These vectors were saved and searched using
ChromaDB, a lightweight vector database. All coding and
testing were done in Google Colab. For example, when we
searched for &quot;high blood pressure treatment,&quot; the system
returned a sentence about &quot;medication for hypertension&quot; -
proving that it could understand medical terms even if they
were worded differently. This kind of system can make it
easier for doctors or medical staff to find relevant
records quickly, especially in electronic health record
systems. Overall, this project shows how machine learning
tools like sentence embeddings can make healthcare data
smarter and more useful.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="deep learning for skin lesion detection: a cnn approach nikunja swain, biswajit biswal, xiaomao liu, janmejay mohanty, jaleel johnson, zy&#x27;aier frazzier, tyler brown skin cancer is one of the most common and fastest-growing cancers worldwide. early and accurate detection is critical to improving patient outcomes, reducing the need for invasive procedures, and lowering mortality rates. this project investigates the application of deep learning, specifically convolutional neural networks (cnns), for the automatic classification of skin lesion images using the ham10000 dataset. the cnn model was trained to recognize and differentiate between seven dermatological conditions: melanoma, basal cell carcinoma (bcc), benign keratosis-like lesions (bkl), actinic keratoses and intraepithelial carcinoma (akiec), dermatofibroma (df), melanocytic nevi (nv), and vascular lesions (vasc). to improve model performance and address class imbalance, preprocessing steps such as image normalization and data augmentation were applied. a custom batch data generator was also implemented to efficiently manage system memory and streamline training. model development was conducted using google colab with tensorflow and keras, leveraging gpu acceleration for faster computation. the resulting cnn achieved a validation accuracy of approximately 85%, placing its performance within the reported dermatologist accuracy range of 62–80%. these results highlight the potential of ai-driven diagnostic tools in assisting with early skin cancer detection and supporting clinical decision-making. the model is especially valuable for deployment in underserved or remote areas where dermatology specialists may not be available. however, further validation is needed to assess its generalizability to real-world clinical settings, including diverse populations and non-dermoscopic images. with continued refinement, this system could significantly enhance screening, diagnosis, and treatment planning in modern dermatology. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_16.pdf">Deep Learning for Skin Lesion Detection: A CNN Approach</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Nikunja Swain, Biswajit Biswal, Xiaomao Liu, Janmejay Mohanty, Jaleel Johnson, Zy&#x27;Aier Frazzier, Tyler Brown</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Skin cancer is one of the most common and fastest-growing
cancers worldwide. Early and accurate detection is critical
to improving patient outcomes, reducing the need for
invasive procedures, and lowering mortality rates. This
project investigates the application of deep learning,
specifically convolutional neural networks (CNNs), for the
automatic classification of skin lesion images using the
HAM10000 dataset. The CNN model was trained to recognize
and differentiate between seven dermatological conditions:
melanoma, basal cell carcinoma (bcc), benign keratosis-like
lesions (bkl), actinic keratoses and intraepithelial
carcinoma (akiec), dermatofibroma (df), melanocytic nevi
(nv), and vascular lesions (vasc). To improve model
performance and address class imbalance, preprocessing
steps such as image normalization and data augmentation
were applied. A custom batch data generator was also
implemented to efficiently manage system memory and
streamline training. Model development was conducted using
Google Colab with TensorFlow and Keras, leveraging GPU
acceleration for faster computation. The resulting CNN
achieved a validation accuracy of approximately 85%,
placing its performance within the reported dermatologist
accuracy range of 62–80%. These results highlight the
potential of AI-driven diagnostic tools in assisting with
early skin cancer detection and supporting clinical
decision-making. The model is especially valuable for
deployment in underserved or remote areas where dermatology
specialists may not be available. However, further
validation is needed to assess its generalizability to
real-world clinical settings, including diverse populations
and non-dermoscopic images. With continued refinement, this
system could significantly enhance screening, diagnosis,
and treatment planning in modern dermatology.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="cardiovascular disease prediction using machine learning nikunja swain, biswajit biswal, xiaomao liu, janmejay mohanty, xavier white, trey newton, blake nichols cardiovascular disease (cvd) remains one of the leading causes of death worldwide, posing a significant challenge to global health systems. early detection and prevention are critical to reducing its impact, yet traditional diagnostic methods often fall short in identifying at-risk individuals before serious complications arise. this project focuses on developing a machine learning-based cardiovascular disease prediction model that can analyze key health indicators and predict individual risk with greater accuracy and efficiency. this aligns closely with the center’s mission to advance health equity through innovative, data-driven solutions. by combining medical knowledge with artificial intelligence, this work embraces the center’s commitment to improving public health outcomes, expanding access to preventive care, and empowering communities through technology-driven healthcare innovation. this project presents a machine learning-based approach for predicting the risk of cardiovascular disease using patient health data. by leveraging algorithms such as logistic regression, random forest, and support vector machines, the system analyzes features including age, blood pressure, cholesterol levels, bmi, and lifestyle factors to assess cardiovascular risk. the dataset, preprocessed for missing values and scaled for consistency, is split into training and testing sets to evaluate model accuracy. performance metrics such as precision, recall, and roc-auc scores are used to determine the most effective model. this predictive tool aims to support early diagnosis and preventive healthcare decisions, offering an accessible, data-driven method for identifying at-risk individuals. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_17.pdf">Cardiovascular Disease Prediction Using Machine Learning</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Nikunja Swain, Biswajit Biswal, Xiaomao Liu, Janmejay Mohanty, Xavier White, Trey Newton, Blake Nichols</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Cardiovascular disease (CVD) remains one of the leading
causes of death worldwide, posing a significant challenge
to global health systems. Early detection and prevention
are critical to reducing its impact, yet traditional
diagnostic methods often fall short in identifying at-risk
individuals before serious complications arise. This
project focuses on developing a machine learning-based
cardiovascular disease prediction model that can analyze
key health indicators and predict individual risk with
greater accuracy and efficiency. This aligns closely with
the center’s mission to advance health equity through
innovative, data-driven solutions. By combining medical
knowledge with artificial intelligence, this work embraces
the center’s commitment to improving public health
outcomes, expanding access to preventive care, and
empowering communities through technology-driven healthcare
innovation.
This project presents a machine learning-based approach for
predicting the risk of cardiovascular disease using patient
health data. By leveraging algorithms such as Logistic
Regression, Random Forest, and Support Vector Machines, the
system analyzes features including age, blood pressure,
cholesterol levels, BMI, and lifestyle factors to assess
cardiovascular risk. The dataset, preprocessed for missing
values and scaled for consistency, is split into training
and testing sets to evaluate model accuracy. Performance
metrics such as precision, recall, and ROC-AUC scores are
used to determine the most effective model. This predictive
tool aims to support early diagnosis and preventive
healthcare decisions, offering an accessible, data-driven
method for identifying at-risk individuals.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="xai-drl based intrusion detection system for connected autonomous vehicles felicia forrester, dr. pratap sahu connected autonomous vehicles (cavs) rely heavily on in-vehicle communication systems, the controller area network (can) bus being one, making them increasingly vulnerable to sophisticated cyberattacks. existing intrusion detection systems (ids) for cavs often struggle with real-time detection, limited adaptability to recognize emerging attack patterns, and a lack of transparency in decision making. these limitations reduce trust and effectiveness in safety critical environments. this research proposes an explainable artificial intelligence–deep reinforcement learning (xai-drl) based intrusion detection system designed to address these challenges. the proposed framework leverages deep reinforcement learning to adaptively detect cyber threats in real time while integrating explainable ai techniques to provide clear and interpretable insights into model decisions. using simulation-based testbeds and benchmark datasets, the system evaluates performance across metrics including accuracy, f1-score, response time, and interpretability. the ids assigns vulnerability scores, recommends mitigation actions, and prioritizes system safety with minimal intervention. by combining adaptability with transparency, this work aims to advance the development of scalable, trustworthy, and real-time cybersecurity solutions for connected autonomous vehicles, while also contributing to broader educational and research dissemination efforts. implementation and future work will focus on integrating existing drl models with xai techniques in a python-based simulation environment, refining real-time threat detection, and fully integrating explainable ai into the drl framework. further efforts will explore scalability for larger cav networks and optimize adaptive decision-making to enhance overall system safety with minimal human intervention. poster student - undergraduate poster">
  <h4>XAI-DRL based intrusion detection system for Connected
Autonomous Vehicles</h4>
  <div class="paper-meta"><strong>Authors:</strong> Felicia Forrester, Dr. Pratap Sahu</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Connected Autonomous Vehicles (CAVs) rely heavily on
in-vehicle communication systems, the Controller Area
Network (CAN) bus being one, making them increasingly
vulnerable to sophisticated cyberattacks. Existing
intrusion detection systems (IDS) for CAVs often struggle
with real-time detection, limited adaptability to recognize
emerging attack patterns, and a lack of transparency in
decision making. These limitations reduce trust and
effectiveness in safety critical environments. This
research proposes an Explainable Artificial
Intelligence–Deep Reinforcement Learning (XAI-DRL) based
intrusion detection system designed to address these
challenges. The proposed framework leverages deep
reinforcement learning to adaptively detect cyber threats
in real time while integrating explainable AI techniques to
provide clear and interpretable insights into model
decisions. Using simulation-based testbeds and benchmark
datasets, the system evaluates performance across metrics
including accuracy, F1-score, response time, and
interpretability. The IDS assigns vulnerability scores,
recommends mitigation actions, and prioritizes system
safety with minimal intervention. By combining adaptability
with transparency, this work aims to advance the
development of scalable, trustworthy, and real-time
cybersecurity solutions for connected autonomous vehicles,
while also contributing to broader educational and research
dissemination efforts.
Implementation and future work will focus on integrating
existing DRL models with XAI techniques in a Python-based
simulation environment, refining real-time threat
detection, and fully integrating explainable AI into the
DRL framework. Further efforts will explore scalability for
larger CAV networks and optimize adaptive decision-making
to enhance overall system safety with minimal human
intervention.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="enhancing undergraduate research recruitment through nlp-driven application matching carl bennett in the current academic landscape, the bridge between undergraduate talent and faculty research projects is often built on informal emails or static forms. for professors, reviewing dozens of statements of interest to find specific technical overlaps is time-consuming and ineffective. for students, the lack of transparency in opportunities and how their skills align with them can be a barrier to entry. this project addresses these inefficiencies by providing a centralized, intelligent platform that digitizes recruitment and applies computational linguistics to assist in decision-making. this project follows a decoupled, three-tier architecture designed for scalability and separation of concerns. the frontend utilizes react.js for a dynamic user interface (ui) that provides role-based dashboards. it handles state management for real-time application tracking and provides a responsive environment for both students and professors/principal investigators. the core of the project lies in the backend api, constructed with the django rest framework. django manages the authentication logic, serves as the api gateway, and hosts the machine learning (ml) utility scripts. the relational database, mysql, was chosen for its acid compliance. this ensures that sensitive student data and application records remain consistent and secure. the core feature of this portal is the integration of the scikit-learn library to perform semantic analysis on text data. the matching process follows a three-stage pipeline: pre-processing, vectorization, and similarity scoring. to compare a professor&#x27;s project description with a student&#x27;s statement and resume, the text must be converted into numerical vectors. this is accomplished by using term frequency-inverse document frequency (tf-idf) where tf_{t,d} is the frequency of term t in document d, and the second term is the inverse document frequency, which penalizes common words (like &quot;the&quot; or &quot;and&quot;) while rewarding specific technical terms (like &quot;python&quot; or &quot;microbiology&quot;). once the text is vectorized, the cosine similarity (2) is calculated to determine the distance between the two vectors. this measures the cosine of the angle between them in a high dimensional space. a score of 1.0 (100%) indicates a perfect keyword alignment, while 0.0 indicates no overlap. this project implements several key features to enhance the user experience. by using role-based access control, users are automatically directed to either the student or professor dashboard upon login. keywords in a student&#x27;s statement of interest or resume are highlighted using the tf-idf feature names. the system identifies the top 5 overlapping terms between the student and the project, providing a quick, at-a-glance description of student suitability. applications can be sorted by their keyword alignment immediately, allowing professors to prioritize the most relevant candidates. by moving beyond manual review and adopting nlp-driven matching, this project reduces the administrative friction in undergraduate research. future iterations of this work aim to incorporate large language models (llms) such as gemini or gpt-4 to provide nuanced summaries of student applications and support multilingual sentiment analysis for interdisciplinary projects. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_26.pdf">Enhancing Undergraduate Research Recruitment through
NLP-Driven Application Matching</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Carl Bennett</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">In the current academic landscape, the bridge between
undergraduate talent and faculty research projects is often
built on informal emails or static forms. For professors,
reviewing dozens of statements of interest to find specific
technical overlaps is time-consuming and ineffective. For
students, the lack of transparency in opportunities and how
their skills align with them can be a barrier to entry.
This project addresses these inefficiencies by providing a
centralized, intelligent platform that digitizes
recruitment and applies computational linguistics to assist
in decision-making.
This project follows a decoupled, three-tier architecture
designed for scalability and separation of concerns. The
frontend utilizes React.js for a  dynamic User Interface
(UI) that provides role-based dashboards. It handles state
management for real-time application tracking and provides
a responsive environment for both students and
professors/Principal Investigators. The core of the project
lies in the backend API, constructed with the Django REST
Framework. Django manages the authentication logic, serves
as the API gateway, and hosts the Machine Learning (ML)
utility scripts. The relational database, MySQL, was chosen
for its ACID compliance. This ensures that sensitive
student data and application records remain consistent and
secure. The core feature of this portal is the integration
of the scikit-learn library to perform semantic analysis on
text data. The matching process follows a three-stage
pipeline: Pre-processing, Vectorization, and Similarity
Scoring. To compare a professor&#x27;s project description with
a student&#x27;s statement and Resume, the text must be
converted into numerical vectors. This is accomplished by
using Term Frequency-Inverse Document Frequency (TF-IDF)
Where tf_{t,d} is the frequency of term t in document d,
and the second term is the Inverse Document Frequency,
which penalizes common words (like &quot;the&quot; or &quot;and&quot;) while
rewarding specific technical terms (like &quot;Python&quot; or
&quot;Microbiology&quot;).
Once the text is vectorized, the Cosine Similarity (2) is
calculated to determine the distance between the two
vectors. This measures the cosine of the angle between them
in a high dimensional space. A score of 1.0 (100%)
indicates a perfect keyword alignment, while 0.0 indicates
no overlap.

This project implements several key features to enhance the
user experience. By using Role-Based Access Control, Users
are automatically directed to either the Student or
Professor dashboard upon login. Keywords in a student&#x27;s
statement of interest or resume are highlighted using the
TF-IDF feature names. The system identifies the top 5
overlapping terms between the student and the project,
providing a quick, at-a-glance description of student
suitability. Applications can be sorted by their keyword
alignment immediately, allowing professors to prioritize
the most relevant candidates.
By moving beyond manual review and adopting NLP-driven
matching, this project reduces the administrative friction
in undergraduate research. Future iterations of this work
aim to incorporate Large Language Models (LLMs) such as
Gemini or GPT-4 to provide nuanced summaries of student
applications and support multilingual sentiment analysis
for interdisciplinary projects.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="decal management system chante ray abstract—the decal management system is designed to modernize and streamline the process of vehicle decal registration within a university environment. some universities currently rely on manual or paper-based systems for issuing parking decals, leading to delays and administrative burdens. this project introduces a web-based application that enables students, faculty, and staff to apply for, pay for, and manage vehicle decals securely online. this application reduces paperwork, improves accessibility, and enhances administrative efficiency while maintaining strong data integrity and security standards. poster student - undergraduate poster">
  <h4>Decal Management System</h4>
  <div class="paper-meta"><strong>Authors:</strong> Chante Ray</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">REJECT Poster</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Abstract—The Decal Management System is designed to
modernize and streamline the process of vehicle decal
registration within a university environment. Some
universities currently rely on manual or paper-based
systems for issuing parking decals, leading to delays and
administrative burdens. This project introduces a web-based
application that enables students, faculty, and staff to
apply for, pay for, and manage vehicle decals securely
online. This application reduces paperwork, improves
accessibility, and enhances administrative efficiency while
maintaining strong data integrity and security standards.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="assessing video llm performance in detecting child safety risks amaya keys, saurav keshari aryal, gloria washington traditional baby monitoring devices serve as a cautionary tool for parents, guardians, and caregivers concerned about the safety and security of their child; however, they require constant and scrutinous supervision. with ever-so-persistent distractions and responsibilities, as well as the inevitable need for rest, humans do not have the luxury of around-the-clock surveillance. this preliminary study introduces the use of large language models (llms) to develop an artificial intelligence (ai)-enabled baby monitoring system that identifies when a child is engaging in unsafe behavior requiring adult attention. forty-five use-case videos of children engaging in either dangerous or age-appropriate activity were fed into two video understanding llms: qwen2-vl and video-llava. a sliding window approach was employed to simulate live video streaming. both models were prompted to process the video input and return the first instance of danger detected. the outcomes were compared against human perception to identify maximal detection accuracy. qwen’s accuracy matched human perception on 31/45 videos by the second and 29/45 videos by the frame, yielding a 67% average accuracy rate. llava’s accuracy matched human perception on 23/45 videos by the second and frame, yielding a 51% accuracy rate. results demonstrate that the use of ai in child danger detection is highly feasible, and qwen2-vl presented itself as the superior model for this task. future work aims to supply the model with context from previous windows, perform fine-tuning, and collect data from additional observers to further refine accuracy and precision in preparation for deployment to a fully operational device. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_30.pdf">Assessing Video LLM Performance in Detecting Child Safety
Risks</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Amaya Keys, Saurav Keshari Aryal, Gloria Washington</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Traditional baby monitoring devices serve as a cautionary
tool for parents, guardians, and caregivers concerned about
the safety and security of their child; however, they
require constant and scrutinous supervision. With
ever-so-persistent distractions and responsibilities, as
well as the inevitable need for rest, humans do not have
the luxury of around-the-clock surveillance. This
preliminary study introduces the use of large language
models (LLMs) to develop an artificial intelligence
(AI)-enabled baby monitoring system that identifies when a
child is engaging in unsafe behavior requiring adult
attention. Forty-five use-case videos of children engaging
in either dangerous or age-appropriate activity were fed
into two video understanding LLMs: Qwen2-VL and
Video-LLaVa. A sliding window approach was employed to
simulate live video streaming. Both models were prompted to
process the video input and return the first instance of
danger detected. The outcomes were compared against human
perception to identify maximal detection accuracy. Qwen’s
accuracy matched human perception on 31/45 videos by the
second and 29/45 videos by the frame, yielding a 67%
average accuracy rate. LLaVa’s accuracy matched human
perception on 23/45 videos by the second and frame,
yielding a 51% accuracy rate. Results demonstrate that the
use of AI in child danger detection is highly feasible, and
Qwen2-VL presented itself as the superior model for this
task. Future work aims to supply the model with context
from previous windows, perform fine-tuning, and collect
data from additional observers to further refine accuracy
and precision in preparation for deployment to a fully
operational device.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="understanding object detection vulnerabilities in the age of yolo v11 trinity banks, idongesit mkpong-ruffin, chutima boonthum-denecke, deidre evans object detection models are widely used in technologies such as surveillance, robotics, and autonomous driving. this literature review explores how models like yolov11 have shaped the field while also remaining vulnerable to adversarial attacks. these attacks, including adversarial patches, can cause models to misinterpret images in dangerous ways. by reviewing current research, this paper highlights how these vulnerabilities work, why they matter, and why further study is needed to improve the safety and reliability of modern object detection. object detection models, particularly the &quot;you only look once&quot; (yolo) series, have seen rapid architectural evolution from yolov1 to the current yolov11. while deep learning models are traditionally considered vulnerable to adversarial attacks, this study identifies a significant shift in the effectiveness of these attacks within modern training frameworks. the rapid integration of object detection models into these safety critical domains has made the security of these systems a paramount concern. while previous iterations of the “you only look once” (yolo) architecture have been extensively studied, the transition to the anchor-free model yolov11 presents a new landscape for adversarial robustness. this study performed a comprehensive analysis of established adversarial patch methodologies: the dynamic adversarial patch (dap), which utilized creases transformation (ct) blocks to account for movement, and the remote adversarial patch (ipatch) which seeks to manipulate model semantics from a distance. based on the goal of securing autonomous vehicle environments, this study implemented a custom replication of the ipatch methodology, adapting it from images segmentation to object detection. the experimental framework utilized the bdd100k dataset and employed expectation over transformation (eot) to ensure the patch remained effective across various angles and distances. despite an optimization process spanning 1,000 epochs using the adamax optimizer, the replication failed to achieve the intended adversarial suppression or false-positive results. a significant outcome of this study arose during subsequent robustness testing, where i evaluated yolov11&#x27;s response to various digital perturbations. these experiments revealed that the model consistently and correctly identified the adversarial patches themselves as distinct objects (such as a &quot;teddy bear&quot; or &quot;person&quot;), effectively neutralizing the attack&#x27;s stealth. building directly upon these findings, our future research will pivot to achieving adversarial stealth. our upcoming work will explore the development of patches designed to be semantically hidden from the detection head by incorporating similarity objectives that blend the patch into the environmental background, testing these stealthier boundaries through physical experiments to improve the security of high-stakes technologies. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_31.pdf">Understanding Object Detection Vulnerabilities in the Age
of YOLO v11</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Trinity Banks, Idongesit Mkpong-Ruffin, Chutima Boonthum-Denecke, Deidre Evans</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Object detection models are widely used in technologies
such as surveillance, robotics, and autonomous driving.
This literature review explores how models like YOLOv11
have shaped the field while also remaining vulnerable to
adversarial attacks. These attacks, including adversarial
patches, can cause models to misinterpret images in
dangerous ways. By reviewing current research, this paper
highlights how these vulnerabilities work, why they matter,
and why further study is needed to improve the safety and
reliability of modern object detection. Object detection
models, particularly the &quot;You Only Look Once&quot; (YOLO)
series, have seen rapid architectural evolution from YOLOv1
to the current YOLOv11. While deep learning models are
traditionally considered vulnerable to adversarial attacks,
this study identifies a significant shift in the
effectiveness of these attacks within modern training
frameworks.

The rapid integration of object detection models into these
safety critical domains has made the security of these
systems a paramount concern. While previous iterations of
the “You Only Look Once” (YOLO) architecture have been
extensively studied, the transition to the anchor-free
model YOLOv11 presents a new landscape for adversarial
robustness. This study performed a comprehensive analysis
of established adversarial patch methodologies: the Dynamic
Adversarial Patch (DAP), which utilized Creases
Transformation (CT) blocks to account for movement, and the
Remote Adversarial Patch (IPatch) which seeks to manipulate
model semantics from a distance.

Based on the goal of securing autonomous vehicle
environments, this study implemented a custom replication
of the IPatch methodology, adapting it from images
segmentation to object detection. The experimental
framework utilized the BDD100K dataset and employed
Expectation over Transformation (EoT) to ensure the patch
remained effective across various angles and distances.
Despite an optimization process spanning 1,000 epochs using
the Adamax optimizer, the replication failed to achieve the
intended adversarial suppression or false-positive results.

A significant outcome of this study arose during subsequent
robustness testing, where I evaluated YOLOv11&#x27;s response to
various digital perturbations. These experiments revealed
that the model consistently and correctly identified the
adversarial patches themselves as distinct objects (such as
a &quot;teddy bear&quot; or &quot;person&quot;), effectively neutralizing the
attack&#x27;s stealth. Building directly upon these findings,
our future research will pivot to achieving adversarial
stealth. Our upcoming work will explore the development of
patches designed to be semantically hidden from the
detection head by incorporating similarity objectives that
blend the patch into the environmental background, testing
these stealthier boundaries through physical experiments to
improve the security of high-stakes technologies.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="limitless: the future of personalized ai power sports advertisements luvell glanton for my final class demonstration i created an advertisement using a key frame of a video of me and then altered the image to create a personal and emotional advertisement to show the potential of ai generated personalized advertisements. this project explores the conceptual design of an ai-powered sports advertisement prototype that integrates generative visual techniques and adaptive personalization ideas to examine how artificial intelligence may influence future sports marketing communication. the motivating problem is the growing need for advertisements that resonate with diverse audiences while maintaining creative originality and ethical transparency. sports marketing provides relevant context because visual engagement, identity, and performance symbolism strongly influence audience perception and brand interaction. the project materials consist of conceptual advertisement imagery and illustrative video examples presented in the slides, rather than structured quantitative datasets. inputs therefore include visual design elements, inspirational themes centered on human potential and athletic progression, and exploring demonstrations of ai-assisted image and video transformation. methods are limited to generative and ai-enhanced visual design concepts shown in the presentation, including frame extraction ideas, creative recomposition, and hypothetical personalization workflows. the system workflow emphasizes ideation, visual generation, transformation, and audience-targeting concepts rather than algorithmic optimization or performance evaluation. outcomes are qualitative and prototype-oriented, focusing on narrative coherence, visual symbolism, and perceived adaptability of advertisements rather than numerical metrics. ethical and feasibility considerations are central to the project discussion, including concerns about privacy invasion, financial and energy costs of large-scale ai generation, and the risk of hallucinated or inaccurate outputs. these factors highlight the importance of transparency and responsible deployment in advertising analytics. future work would involve structured data collection and research into audience engagement and retention when viewing a personalized ad generated with ai. also, i would research how measurable evaluation of engagement outcomes between a variety of viewers in different demographics. i would also explore how personalization strategies improve engagement and retention for ads of varying products. additional development would also examine computational efficiency, bias mitigation, and clearer frameworks for in order to keep ai use in sports advertising ethical. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_32.pdf">Limitless: The future of Personalized AI power sports
advertisements</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Luvell Glanton</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">For my final class demonstration I created an advertisement
using a key frame of a video of me and then altered the
image to create a personal and emotional advertisement to
show the potential of AI generated personalized
advertisements. This project explores the conceptual design
of an AI-powered sports advertisement prototype that
integrates generative visual techniques and adaptive
personalization ideas to examine how artificial
intelligence may influence future sports marketing
communication. The motivating problem is the growing need
for advertisements that resonate with diverse audiences
while maintaining creative originality and ethical
transparency. Sports marketing provides relevant context
because visual engagement, identity, and performance
symbolism strongly influence audience perception and brand
interaction.
The project materials consist of conceptual advertisement
imagery and illustrative video examples presented in the
slides, rather than structured quantitative datasets.
Inputs therefore include visual design elements,
inspirational themes centered on human potential and
athletic progression, and exploring demonstrations of
AI-assisted image and video transformation. Methods are
limited to generative and AI-enhanced visual design
concepts shown in the presentation, including frame
extraction ideas, creative recomposition, and hypothetical
personalization workflows. The system workflow emphasizes
ideation, visual generation, transformation, and
audience-targeting concepts rather than algorithmic
optimization or performance evaluation.
Outcomes are qualitative and prototype-oriented, focusing
on narrative coherence, visual symbolism, and perceived
adaptability of advertisements rather than numerical
metrics. Ethical and feasibility considerations are central
to the project discussion, including concerns about privacy
invasion, financial and energy costs of large-scale AI
generation, and the risk of hallucinated or inaccurate
outputs. These factors highlight the importance of
transparency and responsible deployment in advertising
analytics.
Future work would involve structured data collection and
research into audience engagement and retention when
viewing a personalized ad generated with AI. Also, I would
research how measurable evaluation of engagement outcomes
between a variety of viewers in different demographics. I
would also explore how personalization strategies improve
engagement and retention for Ads of varying products.
Additional development would also examine computational
efficiency, bias mitigation, and clearer frameworks for in
order to keep AI use in sports advertising ethical.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="optimizing lineup styles: a data-driven approach to team performance and win probability santiago soto, patrick lucey authors: santiago soto and dr. patrick lucey affiliation: morehouse college and stats perform email: santiago.soto@morehouse.edu problem statement: this ongoing research develops a predictive framework to analyze five-man lineup efficiency and identify player combinations that maximize net rating and win probability. by prioritizing collective unit performance over isolated individual metrics, the study provides actionable data for algorithmic coaching strategies and roster optimization. data description: the analysis leverages a tabular dataset of play-by-play basketball data featuring 9,437 unique lineups across 30 teams. to ensure statistical significance and minimize noise, a threshold of 20 sequences (possessions) per lineup was applied. key features include offensive/defensive ratings, rebounding percentage, and steal rate. methods and analytical approach • feature engineering: performance is normalized per 100 sequences to calculate net rating (net = off - def). • weighted aggregation: team strength is computed through a weighted average of lineup metrics based on frequency of use. • predictive simulation engine: an interactive engine was developed using scaling factors to ensure projections align with league-wide targets. • correlation analysis: a linear regression model assessed the relationship between net score and win percentage. key findings or outcomes • statistical correlation: regression analysis confirmed a near-perfect correlation (r = 0.96) between a team’s net score and its winning percentage. • efficiency tiers: the model successfully classifies units into above/below average efficiency based on league-wide medians. • defensive edge: &quot;good&quot; lineups are distinguished by their ability to consistently limit opponent scoring, whereas weaker teams allow more points despite higher offensive outputs. • win probability: the simulation engine generates win probabilities and projected final scores using weighted averages. impact, implications, and future work: this research develops a framework for optimizing lineups against opponent strength using historical data, though it cannot yet incorporate real-time variables like injuries. future work will expand the simulation with more granular features and multi-season data to assess the long-term stability of high-efficiency lineup styles. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_33.pdf">Optimizing Lineup Styles: A Data-Driven Approach to Team
Performance and Win Probability</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Santiago Soto, Patrick Lucey</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Authors: Santiago Soto and Dr. Patrick Lucey
Affiliation: Morehouse College and Stats Perform
Email: santiago.soto@morehouse.edu
Problem Statement: This ongoing research develops a
predictive framework to analyze five-man lineup efficiency
and identify player combinations that maximize Net Rating
and win probability. By prioritizing collective unit
performance over isolated individual metrics, the study
provides actionable data for algorithmic coaching
strategies and roster optimization.
Data Description: The analysis leverages a tabular dataset
of play-by-play basketball data featuring 9,437 unique
lineups across 30 teams. To ensure statistical significance
and minimize noise, a threshold of 20 sequences
(possessions) per lineup was applied. Key features include
Offensive/Defensive Ratings, Rebounding Percentage, and
Steal Rate.
Methods and Analytical Approach
•	Feature Engineering: Performance is normalized per 100
sequences to calculate Net Rating (Net = Off - Def).
•	Weighted Aggregation: Team strength is computed through a
weighted average of lineup metrics based on frequency of
use.
•	Predictive Simulation Engine: An interactive engine was
developed using scaling factors to ensure projections align
with league-wide targets.
•	Correlation Analysis: A linear regression model assessed
the relationship between net score and win percentage.
Key Findings or Outcomes
•	Statistical Correlation: Regression analysis confirmed a
near-perfect correlation (r = 0.96) between a team’s net
score and its winning percentage.
•	Efficiency Tiers: The model successfully classifies units
into Above/Below Average Efficiency based on league-wide
medians.
•	Defensive Edge: &quot;Good&quot; lineups are distinguished by their
ability to consistently limit opponent scoring, whereas
weaker teams allow more points despite higher offensive
outputs.
•	Win Probability: The simulation engine generates win
probabilities and projected final scores using weighted
averages.
Impact, Implications, and Future Work: This research
develops a framework for optimizing lineups against
opponent strength using historical data, though it cannot
yet incorporate real-time variables like injuries. Future
work will expand the simulation with more granular features
and multi-season data to assess the long-term stability of
high-efficiency lineup styles.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="perfect path: an ai-powered pose detection system for personalized golf swing visualization and inclusive sports engagement corey lewis, mason wallace golf is a sport associated with technical precision and long-term participation. however, access, instruction costs, and social barriers can limit entry for many new players. perfect path explores how computer vision and pose estimation can support individualized swing analysis while lowering barriers through accessible, mobile-based technology. we frame the problem as both a biomechanics challenge, helping users understand body positioning and rotational mechanics, and a design challenge, creating tools that make golf instruction more approachable and data-informed. our system uses user-provided videos as its primary input. through a structured video-to-image workflow, users upload their footage, select a specific key frame, and apply pose detection to extract body lines and joint positions. using python and opencv, the pipeline estimates joint locations, evaluates angles and rotation, and exports a processed skeletal overlay for visualization and comparison. this transforms raw golf footage into interpretable visual feedback focused on alignment, posture, and swing path. the prototype demonstrates a complete end-to-end workflow. first is video upload, second comes frame selection, third is automated pose detection, and lastly, an exportable visualization is provided to the user. importantly, the system does not employ predictive modeling to forecast performance outcomes such as hot distance or scoring improvement. instead, it prioritizes transparent, interpretable visual analytics that allow users to directly observe their mechanics. by avoiding predictions, the tool emphasizes general skill development through self-assessment rather than guiding users to improve on a specific course without raising their overall skill level. from an inclusion perspective, the system is designed to reduce intimidation often experienced by beginners in traditional golf settings. instruction can be costly, socially hierarchical, and reliant on in-person correction. by enabling private, self-paced analysis on a personal device, users can identify and correct mechanical errors without the pressure of public critique. this approach may help create a more welcoming entry point for individuals who feel underrepresented in golf spaces. future development for this project includes a real-time mobile application capable of live swing capture, immediate pose-based feedback, and side-by-side comparison with a built-in reference skeleton. these enhancements would extend usability while maintaining a clear, interpretable analytics framework. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_34.pdf">Perfect Path: An AI-Powered Pose Detection System for
Personalized Golf Swing Visualization and Inclusive Sports
Engagement</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Corey Lewis, Mason Wallace</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Golf is a sport associated with technical precision and
long-term participation. However, access, instruction
costs, and social barriers can limit entry for many new
players. Perfect Path explores how computer vision and pose
estimation can support individualized swing analysis while
lowering barriers through accessible, mobile-based
technology. We frame the problem as both a biomechanics
challenge, helping users understand body positioning and
rotational mechanics, and a design challenge, creating
tools that make golf instruction more approachable and
data-informed.

Our system uses user-provided videos as its primary input.
Through a structured video-to-image workflow, users upload
their footage, select a specific key frame, and apply pose
detection to extract body lines and joint positions. Using
Python and OpenCV, the pipeline estimates joint locations,
evaluates angles and rotation, and exports a processed
skeletal overlay for visualization and comparison. This
transforms raw golf footage into interpretable visual
feedback focused on alignment, posture, and swing path. The
prototype demonstrates a complete end-to-end workflow.
First is video upload, second comes frame selection, third
is automated pose detection, and lastly, an exportable
visualization is provided to the user. Importantly, the
system does not employ predictive modeling to forecast
performance outcomes such as hot distance or scoring
improvement. Instead, it prioritizes transparent,
interpretable visual analytics that allow users to directly
observe their mechanics. By avoiding predictions, the tool
emphasizes general skill development through
self-assessment rather than guiding users to improve on a
specific course without raising their overall skill level.

From an inclusion perspective, the system is designed to
reduce intimidation often experienced by beginners in
traditional golf settings. Instruction can be costly,
socially hierarchical, and reliant on in-person correction.
By enabling private, self-paced analysis on a personal
device, users can identify and correct mechanical errors
without the pressure of public critique. This approach may
help create a more welcoming entry point for individuals
who feel underrepresented in golf spaces. Future
development for this project includes a real-time mobile
application capable of live swing capture, immediate
pose-based feedback, and side-by-side comparison with a
built-in reference skeleton. These enhancements would
extend usability while maintaining a clear, interpretable
analytics framework.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="perfect path: an ai-powered pose detection system for personalized golf swing visualization and inclusive sports engagement mason wallace golf is a sport associated with technical precision and long-term participation. however, access, instruction costs, and social barriers can limit entry for many new players. perfect path explores how computer vision and pose estimation can support individualized swing analysis while lowering barriers through accessible, mobile-based technology. we frame the problem as both a biomechanics challenge, helping users understand body positioning and rotational mechanics, and a design challenge, creating tools that make golf instruction more approachable and data- informed. our system uses user-provided videos as its primary input. through a structured video-to-image workflow, users upload their footage, select a specific key frame, and apply pose detection to extract body lines and joint positions. using python and opencv, the pipeline estimates joint locations, evaluates angles and rotation, and exports a processed skeletal overlay for visualization and comparison. this transforms raw golf footage into interpretable visual feedback focused on alignment, posture, and swing path. the prototype demonstrates a complete end-to-end workflow. first is video upload, second comes frame selection, third is automated pose detection, and lastly, an exportable visualization is provided to the user. importantly, the system does not employ predictive modeling to forecast performance outcomes such as hot distance or scoring improvement. instead, it prioritizes transparent, interpretable visual analytics that allow users to directly observe their mechanics. by avoiding predictions, the tool emphasizes general skill development through self-assessment rather than guiding users to improve on a specific course without raising their overall skill level. from an inclusion perspective, the system is designed to reduce intimidation often experienced by beginners in traditional golf settings. instruction can be costly, socially hierarchical, and reliant on in-person correction. by enabling private, self-paced analysis on a personal device, users can identify and correct mechanical errors without the pressure of public critique. this approach may help create a more welcoming entry point for individuals who feel underrepresented in golf spaces. future development for this project includes a real-time mobile application capable of live swing capture, immediate pose-based feedback, and side-by-side comparison with a built-in reference skeleton. these enhancements would extend usability while maintaining a clear, interpretable analytics framework. poster student - undergraduate poster">
  <h4>Perfect Path: An AI-Powered Pose Detection System for
Personalized Golf Swing Visualization and Inclusive Sports
Engagement</h4>
  <div class="paper-meta"><strong>Authors:</strong> Mason Wallace</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">REJECT Poster</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Golf is a sport associated with technical precision and
long-term participation. However, access,
instruction costs, and social barriers can limit entry for
many new players. Perfect Path explores
how computer vision and pose estimation can support
individualized swing analysis while
lowering barriers through accessible, mobile-based
technology. We frame the problem as both a
biomechanics challenge, helping users understand body
positioning and rotational mechanics,
and a design challenge, creating tools that make golf
instruction more approachable and data-
informed.
Our system uses user-provided videos as its primary input.
Through a structured video-to-image
workflow, users upload their footage, select a specific key
frame, and apply pose detection to
extract body lines and joint positions. Using Python and
OpenCV, the pipeline estimates joint
locations, evaluates angles and rotation, and exports a
processed skeletal overlay for
visualization and comparison. This transforms raw golf
footage into interpretable visual
feedback focused on alignment, posture, and swing path. The
prototype demonstrates a
complete end-to-end workflow. First is video upload, second
comes frame selection, third is
automated pose detection, and lastly, an exportable
visualization is provided to the user.
Importantly, the system does not employ predictive modeling
to forecast performance outcomes
such as hot distance or scoring improvement. Instead, it
prioritizes transparent, interpretable
visual analytics that allow users to directly observe their
mechanics. By avoiding predictions, the
tool emphasizes general skill development through
self-assessment rather than guiding users to
improve on a specific course without raising their overall
skill level.
From an inclusion perspective, the system is designed to
reduce intimidation often experienced
by beginners in traditional golf settings. Instruction can
be costly, socially hierarchical, and
reliant on in-person correction. By enabling private,
self-paced analysis on a personal device,
users can identify and correct mechanical errors without
the pressure of public critique. This
approach may help create a more welcoming entry point for
individuals who feel
underrepresented in golf spaces. Future development for
this project includes a real-time mobile
application capable of live swing capture, immediate
pose-based feedback, and side-by-side
comparison with a built-in reference skeleton. These
enhancements would extend usability
while maintaining a clear, interpretable analytics
framework.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="fine-tuning distilbert, deberta and modernbert for valence–arousal prediction and change estimation araj shah, saurav keshari aryal, utsav shah, gloria washington we propose a unified, lightweight, and reproducible set of models for longitudinal valence–arousal (va) modeling in a corpus of essays written over time by u.s. service-industry workers. using only the official semeval 2026 task 2 data, we enforce user-disjoint splits to prevent leakage and ensure comparable evaluation. we decompose va modeling into three complementary prediction views: (i) per-essay va state estimation from text, (ii) short-horizon user-level va change forecasting from recent history, and (iii) longer-horizon disposition-change prediction from aggregated user histories. for essay-level state estimation, we fine-tune a distilbert encoder with a lightweight regression head. for short-horizon forecasting, we pair modernbert-based text representations with trajectory-derived numeric features and blend a simple previous-delta baseline with a gru sequence regressor over recent embeddings. for longer-horizon disposition modeling, we pool deberta-based user-history embeddings, augment them with normalized summary features, and apply a compact mlp regressor. on the official evaluation, we obtain subtask 1 (essay-level state) composite pearson r = 0.665 (valence), 0.468 (arousal) (official baseline: 0.557, 0.299); subtask 2a (short-horizon change) pearson r = 0.597 (valence), 0.413 (arousal) (official baseline: 0.615, 0.670); and subtask 2b (disposition change) pearson r = 0.046 (valence), 0.348 (arousal) (official baseline: 0.434, 0.584). across all settings, we prioritize strict split control and transparent inference pipelines to make results easy to reproduce and extend, providing a reliable foundation for future work on longitudinal emotion dynamics. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_36.pdf">Fine-Tuning DistilBERT, DeBERTa and ModernBERT for
Valence–Arousal Prediction and Change Estimation</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Araj Shah, Saurav Keshari Aryal, Utsav Shah, Gloria Washington</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">We propose a unified, lightweight, and reproducible set of
models for longitudinal valence–arousal (VA) modeling in a
corpus of essays written over time by U.S. service-industry
workers. Using only the official SemEval 2026 Task 2 data,
we enforce user-disjoint splits to prevent leakage and
ensure comparable evaluation. We decompose VA modeling into
three complementary prediction views: (i) per-essay VA
state estimation from text, (ii) short-horizon user-level
VA change forecasting from recent history, and (iii)
longer-horizon disposition-change prediction from
aggregated user histories. For essay-level state
estimation, we fine-tune a DistilBERT encoder with a
lightweight regression head. For short-horizon forecasting,
we pair ModernBERT-based text representations with
trajectory-derived numeric features and blend a simple
previous-delta baseline with a GRU sequence regressor over
recent embeddings. For longer-horizon disposition modeling,
we pool DeBERTa-based user-history embeddings, augment them
with normalized summary features, and apply a compact MLP
regressor. On the official evaluation, we obtain Subtask 1
(essay-level state) composite Pearson r = 0.665 (valence),
0.468 (arousal) (official baseline: 0.557, 0.299); Subtask
2A (short-horizon change) Pearson r = 0.597 (valence),
0.413 (arousal) (official baseline: 0.615, 0.670); and
Subtask 2B (disposition change) Pearson r = 0.046
(valence), 0.348 (arousal) (official baseline: 0.434,
0.584). Across all settings, we prioritize strict split
control and transparent inference pipelines to make results
easy to reproduce and extend, providing a reliable
foundation for future work on longitudinal emotion dynamics.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="automated estimation of glasgow coma scale scores using multimodal video analysis brent piper, saurav keshari aryal this project explores the feasibility of using multimodal artificial intelligence to estimate glasgow coma scale scores from video observations of patient behavior. the glasgow coma scale is widely used to assess neurological status following injury, but scoring can vary due to observer interpretation and environmental conditions. we investigate whether large multimodal models can assist by analyzing eye opening, verbal response, and motor response directly from video recordings. we developed a workflow that manually preprocesses video clips to isolate patient behavior and reduce bias from narration, overlays, and instructional content. due to the limited availability of single patient recordings, we curated a dataset of manually processed videos and explored controlled scenario generation to test system robustness. preliminary observations suggest that automated analysis can identify key behavioral cues in structured environments while highlighting challenges related to variability and data scarcity. this work contributes an early investigation into how video based ai systems may support clinical training and documentation, emphasizing careful dataset construction and the need for further validation. poster student - undergraduate poster">
  <h4>Automated Estimation of Glasgow Coma Scale Scores Using
Multimodal Video Analysis</h4>
  <div class="paper-meta"><strong>Authors:</strong> Brent Piper, Saurav Keshari Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">REJECT Poster</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This project explores the feasibility of using multimodal
artificial intelligence to estimate Glasgow Coma Scale
scores from video observations of patient behavior. The
Glasgow Coma Scale is widely used to assess neurological
status following injury, but scoring can vary due to
observer interpretation and environmental conditions. We
investigate whether large multimodal models can assist by
analyzing eye opening, verbal response, and motor response
directly from video recordings.

We developed a workflow that manually preprocesses video
clips to isolate patient behavior and reduce bias from
narration, overlays, and instructional content. Due to the
limited availability of single patient recordings, we
curated a dataset of manually processed videos and explored
controlled scenario generation to test system robustness.
Preliminary observations suggest that automated analysis
can identify key behavioral cues in structured environments
while highlighting challenges related to variability and
data scarcity.

This work contributes an early investigation into how video
based AI systems may support clinical training and
documentation, emphasizing careful dataset construction and
the need for further validation.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="time-aware two-dimensional packing for throughput optimization in slicing-aware 3d printing stephone christian, blayne montaque, saurav aryal batching multiple parts onto a single fused-filament fabrication build plate improves throughput, but existing packing algorithms optimize for geometric density rather than print time. we introduce a slicing-aware cost model that estimates print time from part geometry and placement without invoking toolpath generation, achieving strong correlation with slicer-reported times (pearson r = 0.90, spearman ρ = 0.96). evaluating packing algorithms on synthetic production builds, we find that greedy polygon-based packing matches or exceeds large neighborhood search at three orders of magnitude lower compute cost — a negative result we attribute to high initial packing density leaving minimal room for iterative refinement. against prusaslicer’s default auto-arrange, our method achieves 5.7% throughput improvement (95% ci [4.7%, 7.3%], n = 329), with median savings of 19.5 minutes per build. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_38.pdf">Time-Aware Two-Dimensional Packing for Throughput
Optimization in Slicing-Aware 3D Printing</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Stephone Christian, Blayne Montaque, Saurav Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Batching multiple parts onto a single fused-filament
fabrication build plate improves throughput, but existing
packing algorithms optimize for geometric density rather
than print time. We introduce a slicing-aware cost model
that estimates print time from part geometry and placement
without invoking toolpath generation, achieving strong
correlation with slicer-reported times (Pearson r = 0.90,
Spearman ρ = 0.96). Evaluating packing algorithms on
synthetic production builds, we find that greedy
polygon-based packing matches or exceeds Large Neighborhood
Search at three orders of magnitude lower compute cost — a
negative result we attribute to high initial packing
density leaving minimal room for iterative refinement.
Against PrusaSlicer’s default auto-arrange, our method
achieves 5.7% throughput improvement (95% CI [4.7%, 7.3%],
N = 329), with median savings of 19.5 minutes per build.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="disaster relief ai chatbot ezichi chimezie, blayne montaque, terri adams-fuller, saurav aryal, legand burge during natural disasters, access to timely and reliable information is critical. however, many emergency communication systems depend on continuous internet connectivity or one-way broadcast alerts that can become inaccessible during infrastructure disruptions. this work addresses the need for accessible, conversational access to structured disaster information across multiple delivery channels. we developed a dual-mode conversational chatbot that integrates large language model–driven dialogue with authoritative, structured data services. a gpt-based model interprets natural language queries and routes them to six disaster-relevant services via external apis, including weather conditions, air quality, emergency alerts, road conditions, shelter availability, and geolocation. a local persistence layer supports session management and system coordination. the system provides both web-based and sms-based interfaces, enabling access across different connectivity contexts. the current prototype grounds all responses in verified service outputs, incorporates location-awareness and emergency-detection workflows, and supports multi-intent query handling. ongoing work focuses on improving system robustness, expanding fault tolerance, and preparing the platform for scalable deployment. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_39.pdf">Disaster Relief AI Chatbot</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Ezichi Chimezie, Blayne Montaque, Terri Adams-Fuller, Saurav Aryal, Legand Burge</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">During natural disasters, access to timely and reliable
information is critical. However, many emergency
communication systems depend on continuous internet
connectivity or one-way broadcast alerts that can become
inaccessible during infrastructure disruptions. This work
addresses the need for accessible, conversational access to
structured disaster information across multiple delivery
channels.

We developed a dual-mode conversational chatbot that
integrates large language model–driven dialogue with
authoritative, structured data services. A GPT-based model
interprets natural language queries and routes them to six
disaster-relevant services via external APIs, including
weather conditions, air quality, emergency alerts, road
conditions, shelter availability, and geolocation. A local
persistence layer supports session management and system
coordination. The system provides both web-based and
SMS-based interfaces, enabling access across different
connectivity contexts.

The current prototype grounds all responses in verified
service outputs, incorporates location-awareness and
emergency-detection workflows, and supports multi-intent
query handling. Ongoing work focuses on improving system
robustness, expanding fault tolerance, and preparing the
platform for scalable deployment.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="exploring prompt strategies for joke generation under input constraints abdulmujeeb lawal, saurav keshari aryal a number of studies have explored what makes jokes funny. conversely, only a few have actually tackled generating them, mostly leaving humor-generation relatively unexplored. the semeval mwahaha challenge tasks participants with generating jokes under different constraints with the aim of pushing models beyond memorization towards genuine joke creation. in subtask a, inputs were either keyword pairs or news headlines, and jokes had to incorporate both keywords or draw from the given headline. for headlines, we prompted the model to write reaction-style tweets, which produced more natural humor, while for the keyword pairs, we had the model adopt dave chappelle&#x27;s comedic persona to create observational jokes about some everyday situations and disappointments. we experimented primarily with open-source models (llama and qwen) and ended up using llama for our final submission. in our preliminary results, we found that persona-based prompting consistently outperformed generic prompting approaches. the chappelle-style observational jokes for keyword pairs also seemed to elicit more reactions than the standard outputs, and the tweet-format jokes for headlines felt more natural and appropriate for the given context. we also observed that models struggled a lot more with keyword pairs than with headlines, most likely because combining two unrelated words into coherent humor may require a bit more creative reasoning. our findings show that tailoring prompting methods based on input type, rather than applying a singular approach, decently improves humor generation. our work also shows the value of using personas when guiding models toward more diverse and naturally funny jokes. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_40.pdf">Exploring Prompt Strategies for Joke Generation Under Input
Constraints</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Abdulmujeeb Lawal, Saurav Keshari Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">A number of studies have explored what makes jokes funny.
Conversely, only a few have actually tackled generating
them, mostly leaving humor-generation relatively
unexplored. The SemEval MWAHAHA Challenge tasks
participants with generating jokes under different
constraints with the aim of pushing models beyond
memorization towards genuine joke creation. In Subtask A,
inputs were either keyword pairs or news headlines, and
jokes had to incorporate both keywords or draw from the
given headline. For headlines, we prompted the model to
write reaction-style tweets, which produced more natural
humor, while for the keyword pairs, we had the model adopt
Dave Chappelle&#x27;s comedic persona to create observational
jokes about some everyday situations and disappointments.
We experimented primarily with open-source models (Llama
and Qwen) and ended up using Llama for our final submission.
In our preliminary results, we found that persona-based
prompting consistently outperformed generic prompting
approaches. The Chappelle-style observational jokes for
keyword pairs also seemed to elicit more reactions than the
standard outputs, and the tweet-format jokes for headlines
felt more natural and appropriate for the given context. We
also observed that models struggled a lot more with keyword
pairs than with headlines, most likely because combining
two unrelated words into coherent humor may require a bit
more creative reasoning.
Our findings show that tailoring prompting methods based on
input type, rather than applying a singular approach,
decently improves humor generation. Our work also shows the
value of using personas when guiding models toward more
diverse and naturally funny jokes.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="speech-based detection and severity assessment of alzheimer’s disease chidubem valentine ezikeoha, saurav keshari aryal, howard prioleau early detection in alzheimer’s remains challenging, as current diagnostic methods rely on clinical expertise, and cognitive testing, which can be costly and inaccessible. because cognitive decline is reflected in speech through changes in vocabulary, readability, pauses, articulation, and prosody, spoken language offers a scalable, low-cost, and non-invasive signal for screening and monitoring. prior work demonstrated good performance in predicting mini-mental state examination (mmse) scores using large acoustic-linguistic feature sets, with optimized lightgbm and ensemble models significantly reducing rmse and achieving strong alzheimer’s detection accuracy. in this work, we extend beyond text-focused modeling toward a multilingual, audio-driven model for dementia detection and severity assessment. we train audio spectrogram transformer (ast) models across adress-style datasets to establish robust audio-only baselines, apply multilingual automatic speech recognition to obtain transcripts, and develop multimodal fusion models that integrate acoustic embeddings with linguistic features. this work lays the foundation for scalable and multilingual speech-based tools that can support early dementia detection. by using both audio and linguistic signals, it moves towards a more accessible approach to identifying cognitive decline. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_41.pdf">Speech-Based Detection and Severity Assessment of
Alzheimer’s Disease</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Chidubem Valentine Ezikeoha, Saurav Keshari Aryal, Howard Prioleau</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Early detection in Alzheimer’s remains challenging, as
current diagnostic methods rely on clinical expertise, and
cognitive testing, which can be costly and inaccessible.
Because cognitive decline is reflected in speech through
changes in vocabulary, readability, pauses, articulation,
and prosody, spoken language offers a scalable, low-cost,
and non-invasive signal for screening and monitoring. Prior
work demonstrated good performance in predicting
Mini-Mental State Examination (MMSE) scores using large
acoustic-linguistic feature sets, with optimized LightGBM
and ensemble models significantly reducing RMSE and
achieving strong Alzheimer’s detection accuracy. In this
work, we extend beyond text-focused modeling toward a
multilingual, audio-driven model for dementia detection and
severity assessment. We train Audio Spectrogram Transformer
(AST) models across ADReSS-style datasets to establish
robust audio-only baselines, apply multilingual automatic
speech recognition to obtain transcripts, and develop
multimodal fusion models that integrate acoustic embeddings
with linguistic features. This work lays the foundation for
scalable and multilingual speech-based tools that can
support early dementia detection. By using both audio and
linguistic signals, it moves towards a more accessible
approach to identifying cognitive decline.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="a.n.t.s. (autonomous, navigation, technician, swarm) luther gourdine, alejandro fountain, blayne montaque, brandon williams, bipul gyawali, somkenechukwu onwusika, kroix jones, kwaku asare, saurav aryal this project addresses aircraft exterior inspections performed between flights to identify cracks, dents, corrosion, and paint erosion. today, these walk-through inspections require significant manpower, can vary by inspector, and may expose technicians to safety risks when accessing elevated or hard-to-reach areas. a.n.t.s. (autonomous, navigation, technician, swarm) proposes an operator-supervised autonomous drone inspection system to improve repeatability, documentation quality, and inspection efficiency while maintaining technicians&#x27; full decision-making authority. our approach uses stable, close-range quadcopter flights around a stationary aircraft to capture high-resolution imagery (with optional depth sensing). collected data is processed on resource-constrained edge hardware using an embedded computer-vision pipeline (yolov8n) to detect defect candidates and automatically generate maintenance-ready inspection reports. to ensure flight safety and real-world reliability, the system includes software-controlled inference throttling to manage power and thermal limits during inspection. so far, we have defined the inspection concept of operations as a decision-support workflow, selected the baseline perception model (yolov8n) and edge-inference strategy, and outlined validation needs for close-proximity navigation near reflective surfaces, varied lighting, and different materials. next steps focus on assembling test imagery, integrating sensors, and running controlled flight and mock-panel defect trials. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_42.pdf">A.N.T.S.  (Autonomous, Navigation, Technician, Swarm)</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Luther Gourdine, Alejandro Fountain, Blayne Montaque, Brandon Williams, Bipul Gyawali, Somkenechukwu Onwusika, Kroix Jones, Kwaku Asare, Saurav Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This project addresses aircraft exterior inspections
performed between flights to identify cracks, dents,
corrosion, and paint erosion. Today, these walk-through
inspections require significant manpower, can vary by
inspector, and may expose technicians to safety risks when
accessing elevated or hard-to-reach areas. A.N.T.S.
(Autonomous, Navigation, Technician, Swarm) proposes an
operator-supervised autonomous drone inspection system to
improve repeatability, documentation quality, and
inspection efficiency while maintaining technicians&#x27; full
decision-making authority.
Our approach uses stable, close-range quadcopter flights
around a stationary aircraft to capture high-resolution
imagery (with optional depth sensing). Collected data is
processed on resource-constrained edge hardware using an
embedded computer-vision pipeline (YOLOv8n) to detect
defect candidates and automatically generate
maintenance-ready inspection reports. To ensure flight
safety and real-world reliability, the system includes
software-controlled inference throttling to manage power
and thermal limits during inspection.
So far, we have defined the inspection concept of
operations as a decision-support workflow, selected the
baseline perception model (YOLOv8n) and edge-inference
strategy, and outlined validation needs for close-proximity
navigation near reflective surfaces, varied lighting, and
different materials. Next steps focus on assembling test
imagery, integrating sensors, and running controlled flight
and mock-panel defect trials.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="evidence guided abductive scoring with option conditioned retrieval and constrained llm evaluation ifeoluwakiitan ayandosu, saurav keshari aryal abductive event reasoning in the wild requires selecting plausible explanations for an event from noisy, partially relevant multi document context. we present an evidence guided abductive scoring pipeline for semeval 2026 task 12 that separates evidence selection from explanation scoring. for each topic, we chunk documents and retrieve option conditioned evidence using dense embeddings, then apply a cross encoder reranker to form compact evidence packs per option. a constrained large language model scorer evaluates each option using only its evidence pack and outputs structured signals capturing evidence support, explanatory directness, and contradiction. we then apply deterministic decision rules to produce single or multi label predictions, including robust handling of none of the above style options through semantic detection rather than reliance on option position. this modular design reduces distraction from irrelevant documents, improves comparability across options, and enables controlled calibration for multi answer outputs. our approach demonstrates that retrieval focused evidence compression combined with disciplined, signal based scoring can effectively support abductive reasoning without explicit knowledge graphs or end to end prompting over full document context. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_43.pdf">Evidence Guided Abductive Scoring with Option Conditioned
Retrieval and Constrained LLM Evaluation</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Ifeoluwakiitan Ayandosu, Saurav Keshari Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Abductive event reasoning in the wild requires selecting
plausible explanations for an event from noisy, partially
relevant multi document context. We present an evidence
guided abductive scoring pipeline for SemEval 2026 Task 12
that separates evidence selection from explanation scoring.
For each topic, we chunk documents and retrieve option
conditioned evidence using dense embeddings, then apply a
cross encoder reranker to form compact evidence packs per
option. A constrained large language model scorer evaluates
each option using only its evidence pack and outputs
structured signals capturing evidence support, explanatory
directness, and contradiction. We then apply deterministic
decision rules to produce single or multi label
predictions, including robust handling of none of the above
style options through semantic detection rather than
reliance on option position. This modular design reduces
distraction from irrelevant documents, improves
comparability across options, and enables controlled
calibration for multi answer outputs. Our approach
demonstrates that retrieval focused evidence compression
combined with disciplined, signal based scoring can
effectively support abductive reasoning without explicit
knowledge graphs or end to end prompting over full document
context.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="unsupervised people’s speech challenge: bimamba2 masked spectrogram model prakriti subedi, saurav keshari aryal, howard prioleau self-supervised speech learning extracts transferable representations from unlabeled audio, which is essential for multilingual settings where transcripts and reliable language annotations are limited. we present a masked spectrogram modeling (msm) system for the unsupervised speech in the wild challenge (ups dataset), open filtering sub-track, with an emphasis on data selection strategies that reduce language imbalance during training. the ups audio pool is large and highly multilingual, but the distribution is skewed toward high-resource languages. to prevent training from being dominated by a small number of languages, we enforce manifest-level balancing for the non-english portion by grouping examples by language and applying a per-language quota (cap) before filling a fixed multilingual budget. in our current setup, no single non-english language contributes more than 4,000 examples to the multilingual manifest, ensuring consistent representation of lower-resource languages throughout training. we train a bimamba2-based msm model on log-mel spectrogram segments (10-second chunks), reconstructing masked time-frequency regions to learn phonetic and speaker structure without supervision. the current training phase uses 200 hours of filtered audio (100 hours english, 100 hours non-english) aligned with the challenge’s few-shot asr, zero-shot language id, and speaker clustering objectives. preliminary results show stable optimization, with validation loss decreasing from approximately 12.0 at early checkpoints (1k–2k steps) to 4.68 at 145k steps, indicating substantially improved reconstruction under multilingual balancing. we plan to scale to larger filtered subsets and evaluate downstream transfer on the challenge metrics. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_44.pdf">Unsupervised People’s Speech Challenge: BiMamba2 Masked
Spectrogram Model</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Prakriti Subedi, Saurav Keshari Aryal, Howard Prioleau</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Self-supervised speech learning extracts transferable
representations from unlabeled audio, which is essential
for multilingual settings where transcripts and reliable
language annotations are limited. We present a masked
spectrogram modeling (MSM) system for the Unsupervised
Speech in the Wild Challenge (UPS dataset), Open Filtering
sub-track, with an emphasis on data selection strategies
that reduce language imbalance during training.
The UPS audio pool is large and highly multilingual, but
the distribution is skewed toward high-resource languages.
To prevent training from being dominated by a small number
of languages, we enforce manifest-level balancing for the
non-English portion by grouping examples by language and
applying a per-language quota (cap) before filling a fixed
multilingual budget. In our current setup, no single
non-English language contributes more than 4,000 examples
to the multilingual manifest, ensuring consistent
representation of lower-resource languages throughout
training.
We train a BiMamba2-based MSM model on log-mel spectrogram
segments (10-second chunks), reconstructing masked
time-frequency regions to learn phonetic and speaker
structure without supervision. The current training phase
uses 200 hours of filtered audio (100 hours English, 100
hours non-English) aligned with the challenge’s Few-Shot
ASR, Zero-Shot Language ID, and Speaker Clustering
objectives. Preliminary results show stable optimization,
with validation loss decreasing from approximately 12.0 at
early checkpoints (1k–2k steps) to 4.68 at 145k steps,
indicating substantially improved reconstruction under
multilingual balancing. We plan to scale to larger filtered
subsets and evaluate downstream transfer on the challenge
metrics.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="evaluating dialect bias in commercial automatic speech recognition systems: a comparative analysis of aave, clean, and noisy speech kennedy gregg, gloria washington, saurav keshari aryal a statistical fairness evaluation using error and semantic similarity metrics kennedy gregg hcai institute, howard university, kennedy.gregg@bison.howard.edu saurav keshari aryal hcai institute, howard university, saurav.aryal@howard.edu gloria washington hcai institute, howard university, gloria.washington@howard.edu this study evaluates eight commercial automatic speech recognition (asr) systems google cloud speech, microsoft azure ai speech, ibm watson speech, deepgram, amazon transcribe, openai speech, assemblyai, and speechmatics across three speech conditions: clean common voice (cv), african american vernacular english (aave), and noisy cv. outputs were compared to human transcripts using word error rate (wer), character error rate (cer), levenshtein distance, and semantic similarity metrics (bert cosine similarity, euclidean distance, jaccard similarity). two-sample t-tests (student’s or welch’s, selected via levene’s test) with benjamini hochberg correction assessed performance differences. all vendors showed statistically significant disparities across all metrics (adjusted p ≈ 0 to &lt; 10⁻⁵⁸). aave speech produced higher error rates and lower semantic similarity than noisy cv, indicating reduced transcription accuracy linked to dialectal variation rather than noise. these findings highlight the need for dialect-aware benchmarking to ensure equitable asr performance. references [1] manu edavakandam, “from audio to words: a python guide to measuring transcription accuracy,”medium,2023. https://medium.com/@manuedavakandam/from-audio-to-words-a-python-guide-to-measuring-transcription-accurracy-f9dd9e70651f poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_46.pdf">Evaluating Dialect Bias in Commercial Automatic Speech
Recognition Systems: A Comparative Analysis of AAVE, Clean,
and Noisy Speech</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Kennedy Gregg, Gloria Washington, Saurav Keshari Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">A Statistical Fairness Evaluation Using Error and Semantic
Similarity Metrics

Kennedy Gregg
HCAI Institute, Howard University,
kennedy.gregg@bison.howard.edu
Saurav Keshari Aryal
HCAI Institute, Howard University, saurav.aryal@howard.edu
Gloria Washington
HCAI Institute, Howard University,
gloria.washington@Howard.edu

This study evaluates eight commercial automatic speech
recognition (ASR) systems Google Cloud Speech, Microsoft
Azure AI Speech, IBM Watson Speech, Deepgram, Amazon
Transcribe, OpenAI Speech, AssemblyAI, and Speechmatics
across three speech conditions: clean Common Voice (CV),
African American Vernacular English (AAVE), and noisy CV.
Outputs were compared to human transcripts using word error
rate (WER), character error rate (CER), Levenshtein
distance, and semantic similarity metrics (BERT cosine
similarity, Euclidean distance, Jaccard similarity).
Two-sample t-tests (Student’s or Welch’s, selected via
Levene’s test) with Benjamini Hochberg correction assessed
performance differences. All vendors showed statistically
significant disparities across all metrics (adjusted p ≈ 0
to &lt; 10⁻⁵⁸). AAVE speech produced higher error rates and
lower semantic similarity than noisy CV, indicating reduced
transcription accuracy linked to dialectal variation rather
than noise. These findings highlight the need for
dialect-aware benchmarking to ensure equitable ASR
performance.

REFERENCES
[1] Manu Edavakandam, “From Audio to Words: A Python Guide
to Measuring Transcription Accuracy,”Medium,2023.
https://medium.com/@manuedavakandam/from-audio-to-words-a-python-guide-to-measuring-transcription-accurracy-f9dd9e70651f</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="improving multilingual medieval handwriting recognition through multimodal language modeling nmachi igwe, saurav keshari aryal, nmachi igwe the automatic recognition of multilingual medieval manuscripts remains a challenging task due to the wide variety of languages and writing styles, making it difficult to achieve consistent analysis. historical documents exhibit grammatical irregularities such as inconsistent spelling and nonstandard grammar, degraded manuscript conditions that have compromised legibility over time, multiple languages written in diverse alphabets, and paleographic complexities, thus rendering conventional ocr(optical character recognition) systems ineffective. using the cmmhwr26 dataset as a source of multilingual medieval manuscript data, we acquire and preprocess manuscript images and their corresponding transcriptions to ensure proper normalization and formatting. our method focuses on training open-weight multimodal language models that integrate visual and textual data to improve handwritten text recognition performance. by leveraging both image-based features and language modeling capabilities, the system aims to achieve robustness and generalization across diverse medieval scripts and languages, including related and linguistically different language families. this work contributes to the development of multilingual historical handwritten text recognition by exploring the use of open-weight multimodal language models in medieval manuscript settings, supporting the creation of more robust systems capable of handling real-world retrodigitization challenges and improving large-scale digitization efforts in the digital humanities. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_48.pdf">Improving Multilingual Medieval Handwriting Recognition
through Multimodal Language Modeling</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Nmachi Igwe, Saurav Keshari Aryal, Nmachi Igwe</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The automatic recognition of multilingual medieval
manuscripts remains a challenging task due to the wide
variety of languages and writing styles, making it
difficult to achieve consistent analysis. Historical
documents exhibit grammatical irregularities such as
inconsistent spelling and nonstandard grammar, degraded
manuscript conditions that have compromised legibility over
time, multiple languages written in diverse alphabets, and
paleographic complexities, thus rendering conventional
OCR(Optical Character Recognition) systems ineffective.
Using the CMMHWR26 dataset as a source of multilingual
medieval manuscript data, we acquire and preprocess
manuscript images and their corresponding transcriptions to
ensure proper normalization and formatting. Our method
focuses on training open-weight multimodal language models
that integrate visual and textual data to improve
handwritten text recognition performance. By leveraging
both image-based features and language modeling
capabilities, the system aims to achieve robustness and
generalization across diverse medieval scripts and
languages, including related and linguistically different
language families. This work contributes to the development
of multilingual historical handwritten text recognition by
exploring the use of open-weight multimodal language models
in medieval manuscript settings, supporting the creation of
more robust systems capable of handling real-world
retrodigitization challenges and improving large-scale
digitization efforts in the digital humanities.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="black press + ai kingston davies, saurav keshari aryal, gloria washington historical newspaper archives are critical for preserving black press history, yet many digitized newspapers exist as fragmented image strips that are difficult to access and study. this fragmentation hinders researchers&#x27; ability to efficiently navigate and analyze these invaluable historical documents. working with the black press archive at howard university, this project addresses this challenge by developing an automated pipeline to reconstruct complete newspaper pages from image strips. using opencv computer vision library, the approach vertically concatenates sequential newspaper strips into complete documents. the system then employs brightness analysis to detect dark horizontal gaps between pages, automatically identifying page boundaries and splitting the stitched image into individual pages. this eliminates manual segmentation work that would otherwise be time-intensive and error-prone. the implemented pipeline successfully processes multiple newspaper strips, generates intermediate stitched outputs for quality verification, and produces organized individual page files. this automation significantly improves the accessibility and usability of the black press archive&#x27;s digitized newspaper collection for historical research and preservation. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_49.pdf">Black Press + AI</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Kingston Davies, Saurav Keshari Aryal, Gloria Washington</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Historical newspaper archives are critical for preserving
Black press history, yet many digitized newspapers exist as
fragmented image strips that are difficult to access and
study. This fragmentation hinders researchers&#x27; ability to
efficiently navigate and analyze these invaluable
historical documents. Working with the Black Press Archive
at Howard University, this project addresses this challenge
by developing an automated pipeline to reconstruct complete
newspaper pages from image strips.
Using OpenCV computer vision library, the approach
vertically concatenates sequential newspaper strips into
complete documents. The system then employs brightness
analysis to detect dark horizontal gaps between pages,
automatically identifying page boundaries and splitting the
stitched image into individual pages. This eliminates
manual segmentation work that would otherwise be
time-intensive and error-prone.
The implemented pipeline successfully processes multiple
newspaper strips, generates intermediate stitched outputs
for quality verification, and produces organized individual
page files. This automation significantly improves the
accessibility and usability of the Black Press Archive&#x27;s
digitized newspaper collection for historical research and
preservation.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="augmenting naval ship images for viewing distance using adobe generative fill clemson nesbeth, saurav keshari aryal, gloria washington, jaye nias, christopher watson, janelle yankey the aim of this project is to assess the ability of a generative ai to produce reasonable and believable images based on the same original images at varying scales to simulate differences in distance from the object. the objects used in this project were varying types of ships. the generated images were assessed in three different ways, all on a scale of high medium and low to measure levels of quality. firstly, background quality which refers to the realism and consistency of the generated image. subject dimensions which refers to how well the generated image preserves the scale and zoom of the ship in the original image. and subject integrity, which referred to the features of the ship and how consistent and believable they were. additionally, we noted whether the original image contained the ship as a whole without any ‘cut off’ parts, and if so, being labelled as “incomplete source”. and lastly was “artifact present” which stated if the generated image had had hallucinations or objects added that were not present in the original image. space was also made for comments to be made on the generated images. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_52.pdf">Augmenting Naval Ship Images for Viewing Distance using
Adobe Generative Fill</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Clemson Nesbeth, Saurav Keshari Aryal, Gloria Washington, Jaye Nias, Christopher Watson, Janelle Yankey</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The aim of this project is to assess the ability of a
generative AI to produce reasonable and believable images
based on the same original images at varying scales to
simulate differences in distance from the object. The
objects used in this project were varying types of ships.
The generated images were assessed in three different ways,
all on a scale of high medium and low to measure levels of
quality.
Firstly, background quality which refers to the realism and
consistency of the generated image.
Subject dimensions which refers to how well the generated
image preserves the scale and zoom of the ship in the
original image.
And subject integrity, which referred to the features of
the ship and how consistent and believable they were.
Additionally, we noted whether the original image contained
the ship as a whole without any ‘cut off’ parts, and if so,
being labelled as “Incomplete source”. And lastly was
“Artifact present” which stated if the generated image had
had hallucinations or objects added that were not present
in the original image. Space was also made for comments to
be made on the generated images.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="advanced methods for top-view rgb-d person re-id (tvrid) bipul gyawali, saurav aryal this paper presents a robust framework for top-view rgb-d person re-identification (tvrid), addressing the specific challenges of the icpr 2026 competition. our approach integrates three specialized tracks: an rgb track utilizing part-based attention and resnet backbones (e.g., vit, swin) to improve robustness to occlusion; a depth track focusing on body-shape cues learned from 1-channel depth with attention and metric losses; and a cross-modal track employing dual-stream fusion with optional cross-attention and cross-modal metric losses. by combining identity (arcface) and metric (batch-hard triplet, center) losses within a pytorch lightning framework, our method achieves strong discriminability across same-camera and cross-passage scenarios. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_53.pdf">Advanced Methods for Top-View RGB-D Person Re-ID (TVRID)</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Bipul Gyawali, Saurav Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This paper presents a robust framework for Top-View RGB-D
Person Re-Identification (TVRID), addressing the specific
challenges of the ICPR 2026 competition. Our approach
integrates three specialized tracks: an RGB track utilizing
part-based attention and ResNet backbones (e.g., ViT, Swin)
to improve robustness to occlusion; a Depth track focusing
on body-shape cues learned from 1-channel depth with
attention and metric losses; and a Cross-Modal track
employing dual-stream fusion with optional cross-attention
and cross-modal metric losses. By combining identity
(ArcFace) and metric (batch-hard triplet, center) losses
within a PyTorch Lightning framework, our method achieves
strong discriminability across same-camera and
cross-passage scenarios.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="knowledge-grounded adverse drug event detection from clinical narratives soluchi fidel-ibeabuchi, saurav aryal, howard prioleau adverse drug events (ades) remain a leading cause of preventable morbidity and healthcare expenditure, yet their identification from electronic health records (ehrs) remains challenging due to the unstructured and context-dependent nature of clinical narratives. while annotated corpora such as the n2c2 dataset support benchmark evaluation, their limited scale and annotation cost constrain generalizability. we present a knowledge-grounded ade detection framework that integrates clinical note extraction with structured pharmacovigilance knowledge from sider. our approach first applies large language model (llm)-based entity and relation extraction to identify drug–event mentions within clinical text. we then incorporate a context-engineering layer that cross-references extracted drug entities against curated side-effect profiles in sider, enabling structured validation of candidate ade associations. this integration reduces spurious drug–event pairings while preserving sensitivity to plausible associations, thereby improving precision without sacrificing recall. by combining biomedical knowledge bases with llm-driven extraction, this work demonstrates a scalable and biologically informed strategy for pharmacovigilance from real-world clinical data. the proposed framework contributes to translational health informatics by bridging curated molecular–drug knowledge and patient-level clinical evidence. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_54.pdf">Knowledge-Grounded Adverse Drug Event Detection from
Clinical Narratives</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Soluchi Fidel-Ibeabuchi, Saurav Aryal, Howard Prioleau</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Adverse Drug Events (ADEs) remain a leading cause of
preventable morbidity and healthcare expenditure, yet their
identification from electronic health records (EHRs)
remains challenging due to the unstructured and
context-dependent nature of clinical narratives. While
annotated corpora such as the n2c2 dataset support
benchmark evaluation, their limited scale and annotation
cost constrain generalizability.
We present a knowledge-grounded ADE detection framework
that integrates clinical note extraction with structured
pharmacovigilance knowledge from SIDER. Our approach first
applies large language model (LLM)-based entity and
relation extraction to identify drug–event mentions within
clinical text. We then incorporate a context-engineering
layer that cross-references extracted drug entities against
curated side-effect profiles in SIDER, enabling structured
validation of candidate ADE associations. This integration
reduces spurious drug–event pairings while preserving
sensitivity to plausible associations, thereby improving
precision without sacrificing recall.
By combining biomedical knowledge bases with LLM-driven
extraction, this work demonstrates a scalable and
biologically informed strategy for pharmacovigilance from
real-world clinical data. The proposed framework
contributes to translational health informatics by bridging
curated molecular–drug knowledge and patient-level clinical
evidence.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="detecting and labeling hidden mpls tunnels madison conley, tristian-connor thomas, anthony nwafor standard traceroute often yields inaccurate internet maps due to mpls tunnels hiding the true path, but this work improves a framework to detect and classify these tunnels—categorized as explicit, implicit, opaque, or invisible—by utilizing two key features: the ttl-propagate status and rfc 4950 extensions. the framework uses the scamper tool to gather essential metadata like the ttl-propagate value and applies three techniques—quoted-ttl signature, opaque tunnel estimation, and invisible tunnel inference—to accurately identify and label all tunnel types poster student - undergraduate poster">
  <h4>Detecting and Labeling Hidden MPLS Tunnels</h4>
  <div class="paper-meta"><strong>Authors:</strong> Madison Conley, Tristian-Connor Thomas, Anthony Nwafor</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">REJECT Poster</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Standard traceroute often yields inaccurate Internet maps
due to MPLS Tunnels
hiding the true path, but this work improves a framework to
detect and classify
these tunnels—categorized as EXPLICIT, IMPLICIT, OPAQUE, or
INVISIBLE—by
utilizing two key features: the ttl-propagate status and
RFC 4950 extensions. The
framework uses the scamper tool to gather essential
metadata like the
ttl-propagate value and applies three techniques—Quoted-TTL
Signature, Opaque
Tunnel Estimation, and Invisible Tunnel Inference—to
accurately identify and label
all tunnel types</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="identification and analysis of missing hops in network routing paths using traceroute and automated python parsing terrell booker, joshua gordon this project investigates the identification and analysis of missing hops in network routing paths using traceroute methodology. three different traceroute tests were conducted to multiple destinations in order to capture variations in hop responses and latency behavior. the resulting traceroute output files were then processed using a custom python script designed to parse the data and extract hop values, response times, and non-responsive nodes. by structuring the traceroute data programmatically, we were able to systematically compare routes, identify patterns in missing hops, and evaluate potential causes such as icmp filtering, network congestion, and routing policies. this automated parsing approach improved accuracy and efficiency in analyzing large traceroute datasets and provided deeper insight into hidden network infrastructure. poster student - undergraduate poster">
  <h4>Identification and Analysis of Missing Hops in Network
Routing Paths Using Traceroute and Automated Python Parsing</h4>
  <div class="paper-meta"><strong>Authors:</strong> Terrell Booker, Joshua Gordon</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">REJECT Poster</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This project investigates the identification and analysis
of missing hops in network routing paths using traceroute
methodology. Three different traceroute tests were
conducted to multiple destinations in order to capture
variations in hop responses and latency behavior. The
resulting traceroute output files were then processed using
a custom Python script designed to parse the data and
extract hop values, response times, and non-responsive
nodes. By structuring the traceroute data programmatically,
we were able to systematically compare routes, identify
patterns in missing hops, and evaluate potential causes
such as ICMP filtering, network congestion, and routing
policies. This automated parsing approach improved accuracy
and efficiency in analyzing large traceroute datasets and
provided deeper insight into hidden network infrastructure.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="filling in the stars - missing hops in traceroute terrell booker, joshua gordon this project investigates the identification and analysis of missing hops in network routing paths using traceroute methodology. because traceroute relies heavily on icmp, many traces contain incomplete hops marked with “*.” to address this limitation, we conducted three traceroute tests and developed a custom python script to parse, align, and compare hop values, response times, and non-responsive nodes. when icmp returned missing hops, the program substituted corresponding udp or tcp responses to create a more complete composite route. our results show that routers often respond selectively based on protocol, confirming that protocol-level filtering significantly affects path visibility. this automated multi-protocol approach improves the accuracy and efficiency of analyzing traceroute data while providing deeper insight into hidden network infrastructure. poster student - undergraduate poster">
  <h4>Filling in the Stars - Missing Hops in Traceroute</h4>
  <div class="paper-meta"><strong>Authors:</strong> Terrell Booker, Joshua Gordon</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">REJECT Poster</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This project investigates the identification and analysis
of missing hops in network routing paths using traceroute
methodology. Because traceroute relies heavily on ICMP,
many traces contain incomplete hops marked with “*.” To
address this limitation, we conducted three traceroute
tests and developed a custom Python script to parse, align,
and compare hop values, response times, and non-responsive
nodes. When ICMP returned missing hops, the program
substituted corresponding UDP or TCP responses to create a
more complete composite route. Our results show that
routers often respond selectively based on protocol,
confirming that protocol-level filtering significantly
affects path visibility. This automated multi-protocol
approach improves the accuracy and efficiency of analyzing
traceroute data while providing deeper insight into hidden
network infrastructure.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="onboard multimodal learning for data-driven decision-making in humanoid robotics olivia rollins, blayne montaque, saurav keshari aryal this work presents the development of a modular bipedal humanoid platform focused on tightly integrating onboard artificial intelligence with multimodal sensor perception for data-driven autonomy. built upon the berkeley humanoid lite architecture, the system emphasizes the unification of mechanical design, embedded compute, and learning-based control within a fully self-contained humanoid framework. we design and implement a multimodal sensor array incorporating lidar, rgb and depth cameras, and microphone inputs, enabling rich environmental perception across spatial and acoustic domains. sensor data are synchronized and fused through a ros 2-based middleware pipeline to produce real-time state estimation, semantic scene understanding, and context-aware environmental representations. these perception outputs inform higher-level decision-making modules, allowing the robot to adapt its locomotion and manipulation strategies based on sensed environmental conditions rather than pre-scripted behaviors. locomotion and task policies are trained in gpu-accelerated simulation and deployed to onboard embedded ai hardware for low-latency inference. this architecture enables closed-loop, perception-driven autonomy without reliance on external compute infrastructure. we evaluate system performance in terms of perception latency, decision consistency, and behavioral adaptability in dynamic indoor environments. the resulting platform demonstrates a scalable approach to embedding ai directly within humanoid robotic systems, enabling real-time, sensor-informed decision-making and advancing the integration of learning-based intelligence in embodied agents. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_60.pdf">Onboard Multimodal Learning for Data-Driven Decision-Making
in Humanoid Robotics</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Olivia Rollins, Blayne Montaque, Saurav Keshari Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This work presents the development of a modular bipedal
humanoid platform focused on tightly integrating onboard
artificial intelligence with multimodal sensor perception
for data-driven autonomy. Built upon the Berkeley Humanoid
Lite architecture, the system emphasizes the unification of
mechanical design, embedded compute, and learning-based
control within a fully self-contained humanoid framework.
We design and implement a multimodal sensor array
incorporating LiDAR, RGB and depth cameras, and microphone
inputs, enabling rich environmental perception across
spatial and acoustic domains. Sensor data are synchronized
and fused through a ROS 2-based middleware pipeline to
produce real-time state estimation, semantic scene
understanding, and context-aware environmental
representations. These perception outputs inform
higher-level decision-making modules, allowing the robot to
adapt its locomotion and manipulation strategies based on
sensed environmental conditions rather than pre-scripted
behaviors.
Locomotion and task policies are trained in GPU-accelerated
simulation and deployed to onboard embedded AI hardware for
low-latency inference. This architecture enables
closed-loop, perception-driven autonomy without reliance on
external compute infrastructure. We evaluate system
performance in terms of perception latency, decision
consistency, and behavioral adaptability in dynamic indoor
environments.
The resulting platform demonstrates a scalable approach to
embedding AI directly within humanoid robotic systems,
enabling real-time, sensor-informed decision-making and
advancing the integration of learning-based intelligence in
embodied agents.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="beyond accuracy: forensic evaluation of trust and grounding in llm outputs christopher watson, janelle yankey, jaye nias, saurav aryal, jeremy blackstone, simone smarr, lucretia williams, gloria washington large language models (llms) are increasingly used in high-stakes decision support to summarize situations, propose actions, and communicate rationale. while these systems often produce fluent and plausible responses, such outputs can obscure uncertainty, weaken grounding, and invite over-reliance by human decision-makers. we present project comprehension, a forensic evaluation framework that examines llm outputs as decision-relevant artifacts rather than isolated answers. the framework combines operationally grounded scenarios with human-centered annotation to assess plausibility, uncertainty signaling, grounding transparency, comprehension support, and actionability. across empirical testing, we find that surface-level response quality is only weakly predictive of grounding transparency: a non-trivial subset of responses appear clear and actionable while providing limited justification or source signaling. these patterns highlight an interpretive risk that is not captured by accuracy-focused evaluation alone. we discuss how forensic evaluation can support trust calibration, assurance practices, and the design of language-enabled decision support systems that better align with human judgment in high-stakes contexts. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_62.pdf">Beyond Accuracy: Forensic Evaluation of Trust and Grounding
in LLM Outputs</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Christopher Watson, Janelle Yankey, Jaye Nias, Saurav Aryal, Jeremy Blackstone, Simone Smarr, Lucretia Williams, Gloria Washington</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Large language models (LLMs) are increasingly used in
high-stakes decision support to summarize situations,
propose actions, and communicate rationale. While these
systems often produce fluent and plausible responses, such
outputs can obscure uncertainty, weaken grounding, and
invite over-reliance by human decision-makers.
We present Project Comprehension, a forensic evaluation
framework that examines LLM outputs as decision-relevant
artifacts rather than isolated answers. The framework
combines operationally grounded scenarios with
human-centered annotation to assess plausibility,
uncertainty signaling, grounding transparency,
comprehension support, and actionability.
Across empirical testing, we find that surface-level
response quality is only weakly predictive of grounding
transparency: a non-trivial subset of responses appear
clear and actionable while providing limited justification
or source signaling. These patterns highlight an
interpretive risk that is not captured by accuracy-focused
evaluation alone.
We discuss how forensic evaluation can support trust
calibration, assurance practices, and the design of
language-enabled decision support systems that better align
with human judgment in high-stakes contexts.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="fine-tuning simam-resnet34 and wavlm-base for cross-lingual speaker verification araj shah, saurav keshari aryal, howard prioleau, gloria washington we present a lightweight, reproducible submission for the tidyvoice 2026 cross-lingual speaker verification challenge implemented in the wespeaker toolkit under single-gpu google colab constraints. our primary system, s1, uses the official simam-resnet34 checkpoint pretrained on voxblink2 and voxceleb2 and fine-tuned on tidyvoicex, which we further fine-tune for five epochs with large-margin classification. in parallel, we implement a secondary self-supervised system, s2, using a frozen wavlm-base frontend with a compact statistics pooling speaker head, trained for four epochs. both systems use standard speech augmentation during training with musan noise and rirs reverberation, while inference uses clean embeddings and cosine scoring. to combine systems, we perform score-level fusion calibrated on a labeled tune-s development split. we z-normalize each system’s tune-s scores using their mean and standard deviation, grid-search a convex fusion weight alpha in the range 0 to 1 with step 0.01 to minimize eer, and apply the frozen normalization and alpha to fuse eval-a (task 1) and eval-u (task 2) score files for submission. on tune-s, s1 substantially outperforms s2, so the selected fusion weight is alpha equals 1.0. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_64.pdf">Fine-Tuning SimAM-ResNet34 and WavLM-Base for Cross-Lingual
Speaker Verification</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Araj Shah, Saurav Keshari Aryal, Howard Prioleau, Gloria Washington</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">We present a lightweight, reproducible submission for the
TidyVoice 2026 cross-lingual speaker verification challenge
implemented in the WeSpeaker toolkit under single-GPU
Google Colab constraints. Our primary system, S1, uses the
official SimAM-ResNet34 checkpoint pretrained on VoxBlink2
and VoxCeleb2 and fine-tuned on TidyVoiceX, which we
further fine-tune for five epochs with large-margin
classification. In parallel, we implement a secondary
self-supervised system, S2, using a frozen WavLM-Base
frontend with a compact statistics pooling speaker head,
trained for four epochs. Both systems use standard speech
augmentation during training with MUSAN noise and RIRS
reverberation, while inference uses clean embeddings and
cosine scoring. To combine systems, we perform score-level
fusion calibrated on a labeled Tune-S development split. We
z-normalize each system’s Tune-S scores using their mean
and standard deviation, grid-search a convex fusion weight
alpha in the range 0 to 1 with step 0.01 to minimize EER,
and apply the frozen normalization and alpha to fuse Eval-A
(Task 1) and Eval-U (Task 2) score files for submission. On
Tune-S, S1 substantially outperforms S2, so the selected
fusion weight is alpha equals 1.0.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="ensemble voting and meta-learning for homonym disambiguation: a hybrid approach to semeval 2026 task 5 kwaku asare, saurav aryal we present a hybrid ensemble approach for semeval 2026 task 5 (ambistory), which requires predicting the plausibility of homonym senses in literary narratives on a 1–5 ordinal scale. the task challenges systems to handle nuanced contextual ambiguity in creative writing, where traditional word sense disambiguation methods often fail. our methodology combines the complementary strengths of large language models and fine-tuned transformers through a multi-stage pipeline. first, we employ diverse llm prompting strategies including few-shot learning, contrastive reasoning, and chain-of-thought prompts across multiple model providers and temperature settings, with optional retrieval-augmented generation to surface relevant training examples. second, we fine-tune roberta-large for ordinal regression using contextualized example sentences, deploying a multi-seed ensemble to reduce prediction variance. third, we apply ensemble voting with median score aggregation across llm outputs to improve prediction robustness. finally, we integrate llm ensemble and roberta predictions through hybrid combination methods: weighted averaging, confidence-based weighting, and a calibrated meta-learner that learns optimal blending strategies from development data. our approach achieves 80% exact-label accuracy and 0.74 spearman correlation on the development set, substantially outperforming baseline methods. the results demonstrate that structured reasoning from llms, when combined with learned transformer representations, ensemble aggregation, and proper calibration, effectively captures the ordinal nature of sense plausibility in complex literary contexts. ablation studies reveal that ensemble voting reduces individual model variance while the meta-learner successfully exploits complementary error patterns between llm and roberta components. future work will explore refined retrieval mechanisms and ensemble optimization strategies. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_65.pdf">Ensemble Voting and Meta-Learning for Homonym
Disambiguation: A Hybrid Approach to SemEval 2026 Task 5</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Kwaku Asare, Saurav Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">We present a hybrid ensemble approach for SemEval 2026 Task
5 (AmbiStory), which requires predicting the plausibility
of homonym senses in literary narratives on a 1–5 ordinal
scale. The task challenges systems to handle nuanced
contextual ambiguity in creative writing, where traditional
Word Sense Disambiguation methods often fail. Our
methodology combines the complementary strengths of large
language models and fine-tuned transformers through a
multi-stage pipeline. First, we employ diverse LLM
prompting strategies including few-shot learning,
contrastive reasoning, and chain-of-thought prompts across
multiple model providers and temperature settings, with
optional retrieval-augmented generation to surface relevant
training examples. Second, we fine-tune RoBERTa-large for
ordinal regression using contextualized example sentences,
deploying a multi-seed ensemble to reduce prediction
variance. Third, we apply ensemble voting with median score
aggregation across LLM outputs to improve prediction
robustness. Finally, we integrate LLM ensemble and RoBERTa
predictions through hybrid combination methods: weighted
averaging, confidence-based weighting, and a calibrated
meta-learner that learns optimal blending strategies from
development data. Our approach achieves 80% exact-label
accuracy and 0.74 Spearman correlation on the development
set, substantially outperforming baseline methods. The
results demonstrate that structured reasoning from LLMs,
when combined with learned transformer representations,
ensemble aggregation, and proper calibration, effectively
captures the ordinal nature of sense plausibility in
complex literary contexts. Ablation studies reveal that
ensemble voting reduces individual model variance while the
meta-learner successfully exploits complementary error
patterns between LLM and RoBERTa components. Future work
will explore refined retrieval mechanisms and ensemble
optimization strategies.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="clustering + adversarial ai kafilat sarki-umar, saurav keshari aryal this paper investigates whether personality type influences a user&#x27;s ability to bypass ai safety guardrails. we construct psychologically grounded personas using gaussian mixture models (gmm) applied to the big five personality dimensions (openness, conscientiousness, extraversion, agreeableness, neuroticism), drawing from the statistical &quot;which character&quot; personality quiz (swcpq) dataset of 2,125 fictional characters rated on 500 personality traits. characters are clustered per big five dimension independently to avoid high-dimensionality issues, with optimal k determined via the elbow method, silhouette scoring, aic, and bic, and validated through bootstrap resampling. each cluster&#x27;s most representative character becomes the blueprint for a persona, yielding p unique ai personas encoded as llm system prompts. these personas systematically probe ai models with restricted prompts, measuring compliance rates and manipulation strategies across personality types. preliminary clustering with k=7 produced balanced groupings with exemplars from works including 10 things i hate about you and the great gatsby, though aic and bic disagreement motivated the shift to big five-aligned clustering. next steps include completing the big five trait mapping, constructing the full persona matrix, and running probing experiments to determine which personality profiles most effectively bypass ai safety guardrails. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_67.pdf">Clustering + Adversarial AI</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Kafilat Sarki-Umar, Saurav Keshari Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This paper investigates whether personality type influences
a user&#x27;s ability to bypass AI safety guardrails. We
construct psychologically grounded personas using Gaussian
Mixture Models (GMM) applied to the Big Five personality
dimensions (Openness, Conscientiousness, Extraversion,
Agreeableness, Neuroticism), drawing from the Statistical
&quot;Which Character&quot; Personality Quiz (SWCPQ) dataset of 2,125
fictional characters rated on 500 personality traits.
Characters are clustered per Big Five dimension
independently to avoid high-dimensionality issues, with
optimal K determined via the elbow method, silhouette
scoring, AIC, and BIC, and validated through bootstrap
resampling. Each cluster&#x27;s most representative character
becomes the blueprint for a persona, yielding P unique AI
personas encoded as LLM system prompts. These personas
systematically probe AI models with restricted prompts,
measuring compliance rates and manipulation strategies
across personality types. Preliminary clustering with K=7
produced balanced groupings with exemplars from works
including 10 Things I Hate About You and The Great Gatsby,
though AIC and BIC disagreement motivated the shift to Big
Five-aligned clustering. Next steps include completing the
Big Five trait mapping, constructing the full persona
matrix, and running probing experiments to determine which
personality profiles most effectively bypass AI safety
guardrails.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="the language family effect: improving african sentiment models through linguistic relatedness selorm kalitsi, saurav aryal, howard prioleau african languages represent one of the world’s most linguistically diverse regions, yet they remain critically under-resourced in natural language processing, limiting the development of equitable and effective language technologies. sentiment analysis for these languages is particularly constrained by scarce labeled data, limited representation in pretrained models, and heavy reliance on translation-based pipelines that introduce cultural and semantic distortion, especially in code-switched contexts. this work extends the afrisenti benchmark with sentiment data from 38 additional african languages and examines how linguistic relatedness, captured through language family structure, can be leveraged to improve multilingual sentiment modeling. we evaluate two complementary approaches: extended task- adaptive pretraining on a large and heterogeneous multilingual dataset, and direct language and family conditioning through explicit input-level metadata. experiments conducted at the overall, language family, and individual language levels show that task-adaptive pretraining provides strong gains in large and noisy multilingual settings, while direct language and family conditioning is most effective on smaller and cleaner benchmarks such as afrisenti. together, these results provide empirical evidence for the language family effect, demonstrating that both implicit and explicit modeling of genealogical relationships improves robustness and generalization for african languages that are underrepresented or absent in standard pretrained models. our findings highlight the value of linguistically grounded and data- efficient approaches for building more inclusive and sustainable nlp systems for african languages. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_68.pdf">THE LANGUAGE FAMILY EFFECT: IMPROVING AFRICAN SENTIMENT
MODELS THROUGH LINGUISTIC RELATEDNESS</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Selorm Kalitsi, Saurav Aryal, Howard Prioleau</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">African languages represent one of the world’s most
linguistically diverse regions, yet they
remain critically under-resourced in Natural Language
Processing, limiting the development
of equitable and effective language technologies. Sentiment
analysis for these languages is
particularly constrained by scarce labeled data, limited
representation in pretrained models,
and heavy reliance on translation-based pipelines that
introduce cultural and semantic
distortion, especially in code-switched contexts. This work
extends the AfriSenti benchmark
with sentiment data from 38 additional African languages
and examines how linguistic
relatedness, captured through language family structure,
can be leveraged to improve
multilingual sentiment modeling. We evaluate two
complementary approaches: extended task-
adaptive pretraining on a large and heterogeneous
multilingual dataset, and direct language
and family conditioning through explicit input-level
metadata. Experiments conducted at the
overall, language family, and individual language levels
show that task-adaptive pretraining
provides strong gains in large and noisy multilingual
settings, while direct language and family
conditioning is most effective on smaller and cleaner
benchmarks such as AfriSenti. Together,
these results provide empirical evidence for the language
family effect, demonstrating that both
implicit and explicit modeling of genealogical
relationships improves robustness and
generalization for African languages that are
underrepresented or absent in standard
pretrained models. Our findings highlight the value of
linguistically grounded and data-
efficient approaches for building more inclusive and
sustainable NLP systems for African
languages.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="beyond visible spectrum: developing computer vision techniques for agricultural hyperspectral image categorization todd perkins, saurav aryal technology revolving around remote sensing is being utilized to effectively identify crop diseases in agricultural areas. crop diseases such as fungal, bacterial, and other infections impact agricultural productivity, which can reduce plant growth and nutritional value in everyday food. throughout past research, advances in digital imaging have led researchers to developing methods for seeking potential in crop disease diagnosis through rgb imagery, hyperspectral data, and multispectral analysis. however, the vast number of spectral bands and relationships in remote sensory can pose a challenge to effectively select features and extract data. that is where we come in as we are currently in the process of creating deep learning algorithms to negate those situations. the approach i have come to take is through developing a complex file discovery and reading pipeline to accurately read agricultural data based on the image and file type. my script for containing specific files such as tif, png, and csv finds the file, analyzes the image, and then extracts the data to give statistics and previews. i have made this happen through utilizing opencv, pandas, rasterio, and pathlib to accomplish this. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_69.pdf">Beyond Visible Spectrum: Developing Computer Vision
Techniques for Agricultural Hyperspectral Image
Categorization</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Todd Perkins, Saurav Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Technology revolving around remote sensing is being
utilized to effectively identify crop diseases in
agricultural areas. Crop diseases such as fungal,
bacterial, and other infections impact agricultural
productivity, which can reduce plant growth and nutritional
value in everyday food. Throughout past research, advances
in digital imaging have led researchers to developing
methods for seeking potential in crop disease diagnosis
through RGB imagery, hyperspectral data, and multispectral
analysis. However, the vast number of spectral bands and
relationships in remote sensory can pose a challenge to
effectively select features and extract data. That is where
we come in as we are currently in the process of creating
deep learning algorithms to negate those situations. The
approach I have come to take is through developing a
complex file discovery and reading pipeline to accurately
read agricultural data based on the image and file type. My
script for containing specific files such as TIF, PNG, and
CSV finds the file, analyzes the image, and then extracts
the data to give statistics and previews. I have made this
happen through utilizing OpenCV, pandas, rasterio, and
pathlib to accomplish this.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="query reformulation and dense-lexical retrieval fusion for multi-turn retrieval-augmented generation sijan shrestha, saurav aryal while large language models increasingly serve as chat-based assistants, grounding their responses in retrieved evidence across multi-turn conversations remains a significant challenge, particularly when questions reference earlier turns, when the system must recognize unanswerable queries rather than hallucinate, and when relevant passages shift as the conversation evolves. we address these challenges on the mtrag benchmark across four domain-specific corpora: clapnq (wikipedia), cloud (technical documentation), fiqa (financial), and govt (government web pages). our system employs a hybrid retrieve-then-rerank architecture. queries are first augmented through llm-driven query rewriting, breaking down entities and query itself, and generating hypothetical embeddings (hyde) for semantic matching. results from dense vector search and lexical matching are then fused via reciprocal rank fusion and reranked though cross-encoder. llama-3.3-70b-instruct then generates responses based strictly on the most relevant text passages. the system achieves an ndcg@5 of 0.4098 on passage retrieval, a harmonic mean of 0.7462 on reference-grounded generation, and 0.5796 on end-to-end rag. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_70.pdf">Query Reformulation and Dense-Lexical Retrieval Fusion for
Multi-Turn Retrieval-Augmented Generation</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Sijan Shrestha, Saurav Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">While large language models increasingly serve as
chat-based assistants, grounding their responses in
retrieved evidence across multi-turn conversations remains
a significant challenge, particularly when questions
reference earlier turns, when the system must recognize
unanswerable queries rather than hallucinate, and when
relevant passages shift as the conversation evolves. We
address these challenges on the MTRAG benchmark across four
domain-specific corpora: ClapNQ (Wikipedia), Cloud
(technical documentation), FiQA (financial), and Govt
(government web pages). Our system employs a hybrid
retrieve-then-rerank architecture. Queries are first
augmented through LLM-driven query rewriting, breaking down
entities and query itself, and generating hypothetical
embeddings (HyDE) for semantic matching. Results from dense
vector search and lexical matching are then fused via
Reciprocal Rank Fusion and reranked though cross-encoder.
Llama-3.3-70B-Instruct then generates responses based
strictly on the most relevant text passages. The system
achieves an nDCG@5 of 0.4098 on passage retrieval, a
harmonic mean of 0.7462 on reference-grounded generation,
and 0.5796 on end-to-end RAG.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="artificial intelligence and the expanding digital divide nadia rapheal, e. rebecca caldwell the digital divide has historically separated individuals with reliable access to technology from those without it. as artificial intelligence (ai) becomes increasingly integrated into education, healthcare, business, cybersecurity, and workforce development, this divide is expanding into what can be described as an “ai divide.” individuals in lower socioeconomic communities often lack the technological infrastructure, high-speed broadband access, digital literacy skills, and institutional support necessary to effectively utilize ai tools. in contrast, higher-income communities benefit from stronger internet connectivity, updated hardware, and educational programs that introduce students to emerging technologies. ai systems depend on fast data processing, cloud computing resources, and stable broadband connections to function efficiently. however, high-speed internet services are disproportionately available in urban and suburban areas, while many rural and underserved communities experience slower and less reliable connectivity. this infrastructure gap directly limits access to ai-powered applications used for learning, job training, and economic advancement. educational disparities further intensify the problem. underserved schools often lack funding for advanced computer science courses, ai literacy programs, and updated technological equipment. without early exposure to ai concepts and skills, students may be unprepared for a workforce increasingly shaped by automation and machine learning. as ai expands across industries and begins to automate certain job functions, individuals without access or training risk long-term economic disadvantage. this study examines how infrastructure inequality, limited ai education, and insufficient institutional support may widen socioeconomic gaps in the era of artificial intelligence. it also explores policy and educational strategies designed to promote equitable access to ai technologies and workforce opportunities. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_71.pdf">Artificial Intelligence and the Expanding Digital Divide</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Nadia Rapheal, E. Rebecca Caldwell</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The digital divide has historically separated individuals
with reliable access to technology from those without it.
As Artificial Intelligence (AI) becomes increasingly
integrated into education, healthcare, business,
cybersecurity, and workforce development, this divide is
expanding into what can be described as an “AI divide.”
Individuals in lower socioeconomic communities often lack
the technological infrastructure, high-speed broadband
access, digital literacy skills, and institutional support
necessary to effectively utilize AI tools. In contrast,
higher-income communities benefit from stronger internet
connectivity, updated hardware, and educational programs
that introduce students to emerging technologies.
AI systems depend on fast data processing, cloud computing
resources, and stable broadband connections to function
efficiently. However, high-speed internet services are
disproportionately available in urban and suburban areas,
while many rural and underserved communities experience
slower and less reliable connectivity. This infrastructure
gap directly limits access to AI-powered applications used
for learning, job training, and economic advancement.
Educational disparities further intensify the problem.
Underserved schools often lack funding for advanced
computer science courses, AI literacy programs, and updated
technological equipment. Without early exposure to AI
concepts and skills, students may be unprepared for a
workforce increasingly shaped by automation and machine
learning. As AI expands across industries and begins to
automate certain job functions, individuals without access
or training risk long-term economic disadvantage.
This study examines how infrastructure inequality, limited
AI education, and insufficient institutional support may
widen socioeconomic gaps in the era of artificial
intelligence. It also explores policy and educational
strategies designed to promote equitable access to AI
technologies and workforce opportunities.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="denoising and object tracking in adverse conditions saniya harrigan, saurav aryal, gloria washington the goal of the vistac challenge is to improve visual object tracking under adverse weather conditions. while advanced tracking technologies perform well in controlled and well-lit environments, their performance decreases significantly in challenging conditions such as haze and rain. this limitation is critical because real-world applications, like traffic monitoring systems and autonomous vehicles, must operate reliably in unpredictable environmental settings. the challenge aims to develop robust tracking algorithms capable of maintaining accuracy and consistency in harsh environments. this research investigates the effectiveness of different image denoising and filtering techniques for improving object tracking performances in degraded visual conditions. using annotated video data containing hazy and rainy scenes, multiple preprocessing methods are applied to enhance frame clarity before tracking. the impact of each denoising technique is evaluated based on visual quality, feature preservation, and tracking performance metrics such as qualitative precision (qp) and effective frames per second. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_72.pdf">Denoising and Object Tracking in Adverse Conditions</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Saniya Harrigan, Saurav Aryal, Gloria Washington</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The goal of the VISTAC challenge is to improve visual
object tracking under adverse weather conditions. While
advanced tracking technologies perform well in controlled
and well-lit environments, their performance decreases
significantly in challenging conditions such as haze and
rain. This limitation is critical because real-world
applications, like traffic monitoring systems and
autonomous vehicles, must operate reliably in unpredictable
environmental settings. The challenge aims to develop
robust tracking algorithms capable of maintaining accuracy
and consistency in harsh environments.
This research investigates the effectiveness of different
image denoising and filtering techniques for improving
object tracking performances in degraded visual conditions.
Using annotated video data containing hazy and rainy
scenes, multiple preprocessing methods are applied to
enhance frame clarity before tracking. The impact of each
denoising technique is evaluated based on visual quality,
feature preservation, and tracking performance metrics such
as Qualitative Precision (QP) and effective frames per
second.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="the impact of ai-integrated pre-college bridge program on first-year student success jalia borden, bianca robinson, rebecca caldwell, jacqueline bethea the transition from high school to college can be challenging for many students. college classes are more demanding, schedules are less structured, and students must learn to manage their time independently. many students also feel nervous about meeting new people and adjusting to a new academic environment. to support this transition, many colleges offer pre-college bridge programs that prepare incoming students before their first semester begins. bridge programs focus on building important skills such as time management, study habits, and critical thinking. in our bridge experience, artificial intelligence (ai) tools were also introduced as part of academic preparation. we explored how to use ai responsibly to assist with studying, brainstorming ideas, understanding assignments, and practicing problem-solving. learning how to use ai as a support tool could help freshmen feel more prepared for college-level coursework and more confident in completing assignments. the program bridge provided opportunities to connect with other incoming freshmen and mentors, which could reduced anxiety and helped us build early friendships. in this study, we reflect on how the bridge program—along with guided ai use—improved my academic readiness, confidence, and sense of belonging during our first year. overall, this experience showed that combining traditional bridge support with responsible ai integration can strengthen both academic success and student confidence during the transition to college. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_75.pdf">The Impact of AI-Integrated Pre-College Bridge Program on
First-Year Student Success</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Jalia Borden, Bianca Robinson, Rebecca Caldwell, Jacqueline Bethea</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The transition from high school to college can be
challenging for many students. College classes are more
demanding, schedules are less structured, and students must
learn to manage their time independently. Many students
also feel nervous about meeting new people and adjusting to
a new academic environment. To support this transition,
many colleges offer pre-college bridge programs that
prepare incoming students before their first semester
begins. Bridge programs focus on building important skills
such as time management, study habits, and critical
thinking. In our bridge experience, Artificial Intelligence
(AI) tools were also introduced as part of academic
preparation.
We explored how to use AI responsibly to assist with
studying, brainstorming ideas, understanding assignments,
and practicing problem-solving. Learning how to use AI as a
support tool could help freshmen feel  more prepared for
college-level coursework and more confident in completing
assignments. The program bridge  provided opportunities to
connect with other incoming freshmen and mentors, which
could reduced anxiety and helped us build early
friendships. In this study, we reflect on how the bridge
program—along with guided AI use—improved my academic
readiness, confidence, and sense of belonging during our
first year. Overall, this experience showed that combining
traditional bridge support with responsible AI integration
can strengthen both academic success and student confidence
during the transition to college.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="culturally aware multilingual model routing through a mixture-of-specialists framework isaac adjei, saurav aryal, legand burge large language models (llms) continue to underperform for culturally diverse and linguistically underrepresented communities, limiting their applicability in multilingual and code-switched environments. this work introduces a culturally aware mixture of specialists (mos) framework coordinated by a model control protocol (mcp) server to dynamically route user inputs to language- or region-specific models based on linguistic proximity, cultural relatedness, and data availability. when a dedicated specialist exists, it is used directly; otherwise, a hierarchical fallback strategy selects a linguistically related model, then a culturally proximate variant such as a west african english–tuned specialist, and finally a multilingual backbone augmented with lightweight regional adapters. as part of a multi-phase research program, this paper presents the first stage of the system, focusing on the routing architecture, cultural metadata extraction, and region-aware prompting components while specialist model training is ongoing. to support future specialization, we prepare parameter-efficient fine-tuning pipelines (lora and qlora) using openly licensed corpora rich in local context, including oscar, mc4, bigscience roots, tatoeba, african storybooks, and global voices, with thorough deduplication, filtering, and native-speaker validation. evaluation on the blend benchmark from semeval 2026 task 7 across 26 languages and 30 regions demonstrates that culturally grounded routing signals, regional metadata, and language-specific constraints yield substantial gains in contextual accuracy, robustness in low-resource settings, and cross-regional generalization. these phase-1 results provide early empirical evidence that linguistic relatedness and cultural proximity can meaningfully enhance multilingual model performance even before full specialist integration. overall, this work establishes a scalable foundation for developing globally adaptive and culturally grounded nlp systems. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_76.pdf">CULTURALLY AWARE MULTILINGUAL MODEL ROUTING THROUGH A
MIXTURE-OF-SPECIALISTS FRAMEWORK</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Isaac Adjei, Saurav Aryal, Legand Burge</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Large language models (LLMs) continue to underperform for
culturally diverse and linguistically underrepresented
communities, limiting their applicability in multilingual
and code-switched environments. This work introduces a
culturally aware Mixture of Specialists (MoS) framework
coordinated by a Model Control Protocol (MCP) server to
dynamically route user inputs to language- or
region-specific models based on linguistic proximity,
cultural relatedness, and data availability. When a
dedicated specialist exists, it is used directly;
otherwise, a hierarchical fallback strategy selects a
linguistically related model, then a culturally proximate
variant such as a West African English–tuned specialist,
and finally a multilingual backbone augmented with
lightweight regional adapters. As part of a multi-phase
research program, this paper presents the first stage of
the system, focusing on the routing architecture, cultural
metadata extraction, and region-aware prompting components
while specialist model training is ongoing. To support
future specialization, we prepare parameter-efficient
fine-tuning pipelines (LoRA and QLoRA) using openly
licensed corpora rich in local context, including OSCAR,
mC4, BigScience ROOTS, Tatoeba, African StoryBooks, and
Global Voices, with thorough deduplication, filtering, and
native-speaker validation. Evaluation on the BLEnD
benchmark from SemEval 2026 Task 7 across 26 languages and
30 regions demonstrates that culturally grounded routing
signals, regional metadata, and language-specific
constraints yield substantial gains in contextual accuracy,
robustness in low-resource settings, and cross-regional
generalization. These Phase-1 results provide early
empirical evidence that linguistic relatedness and cultural
proximity can meaningfully enhance multilingual model
performance even before full specialist integration.
Overall, this work establishes a scalable foundation for
developing globally adaptive and culturally grounded NLP
systems.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="asr benchmarking for aave mildness akomoize, saurav aryal, gloria washington automatic speech recognition (asr) systems are widely used in voice assistants, transcription services, and accessibility tools, yet prior research suggests they perform unevenly across dialects. this project investigates performance disparities in commercial asr systems for african american vernacular english (aave). we curated and transcribed over 200 hours of question–response style aave speech data and split it into training, validation, and test sets. using an automated benchmarking pipeline, we evaluate systems including openai whisper, amazon transcribe, and deepgram. performance is measured using word error rate (wer), with statistical analyses such as welch’s t-test and shapiro–wilk tests applied to assess significance and distributional assumptions. preliminary findings indicate that several commercial systems exhibit elevated wer on aave speech relative to reported general benchmarks. to address this gap, we are fine-tuning models on the curated dataset and observing reductions in wer, though this phase remains ongoing. by combining systematic benchmarking, statistical rigor, and dataset development, this work contributes toward more equitable and representative speech recognition technologies poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_77.pdf">ASR Benchmarking for AAVE</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Mildness Akomoize, Saurav Aryal, Gloria Washington</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Automatic speech recognition (ASR) systems are widely used
in voice assistants, transcription services, and
accessibility tools, yet prior research suggests they
perform unevenly across dialects. This project investigates
performance disparities in commercial ASR systems for
African American Vernacular English (AAVE). We curated and
transcribed over 200 hours of question–response style AAVE
speech data and split it into training, validation, and
test sets. Using an automated benchmarking pipeline, we
evaluate systems including OpenAI Whisper, Amazon
Transcribe, and Deepgram. Performance is measured using
Word Error Rate (WER), with statistical analyses such as
Welch’s t-test and Shapiro–Wilk tests applied to assess
significance and distributional assumptions. Preliminary
findings indicate that several commercial systems exhibit
elevated WER on AAVE speech relative to reported general
benchmarks. To address this gap, we are fine-tuning models
on the curated dataset and observing reductions in WER,
though this phase remains ongoing. By combining systematic
benchmarking, statistical rigor, and dataset development,
this work contributes toward more equitable and
representative speech recognition technologies</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="the importance of adversarial patch detection in cybersecurity attacks: a critical analysis of machine learning vulnerabilities and defense mechanisms josiah johnson, e. rebecca caldwell, elva jones adversarial patch detection represents a critical frontier in cybersecurity defense. as artificial intelligence systems assume greater responsibility in safety-critical and security-sensitive applications, the ability to detect and neutralize adversarial attacks becomes paramount. as artificial intelligence systems become increasingly woven into the fabric of critical infrastructure—impacting areas such as autonomous vehicles, facial recognition technologies, medical diagnostics, and financial fraud detection—their vulnerability to adversarial patch attacks takes on a new level of significance, posing a considerable and escalating cybersecurity threat. adversarial patches are intricately designed perturbations, whether physical objects or digital modifications, crafted with precision to deceive ai vision systems. these deceptive alterations can manipulate the system&#x27;s perception and decision-making processes, resulting in erroneous classifications. such manipulation can empower malicious actors to bypass established security measures, take control of autonomous operations, or elude detection mechanisms, potentially leading to catastrophic consequences. this research carefully examines the urgent necessity for adversarial patch detection as an essential component of a comprehensive defensive strategy within the cybersecurity landscape. it explores the increasing sophistication of current adversarial attack methodologies, which often exploit subtle vulnerabilities in ai algorithms with alarming effectiveness. moreover, the study investigates the capabilities of emerging detection frameworks that aim to identify, analyze, and mitigate these sophisticated threats. by exploring the dynamic relationship between advancing adversarial tactics and the evolving defense mechanisms, this work seeks to illuminate strategies to bolster the resilience of ai systems against these insidious attacks, thereby enhancing the safety and reliability of critical infrastructure in a rapidly evolving digital landscape. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_78.pdf">The Importance of Adversarial Patch Detection in
Cybersecurity Attacks: A Critical Analysis of Machine
Learning Vulnerabilities and Defense Mechanisms</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Josiah Johnson, E. Rebecca Caldwell, Elva Jones</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Adversarial patch detection represents a critical frontier
in cybersecurity defense. As artificial intelligence
systems assume greater responsibility in safety-critical
and security-sensitive applications, the ability to detect
and neutralize adversarial attacks becomes paramount. As
artificial intelligence systems become increasingly woven
into the fabric of critical infrastructure—impacting areas
such as autonomous vehicles, facial recognition
technologies, medical diagnostics, and financial fraud
detection—their vulnerability to adversarial patch attacks
takes on a new level of significance, posing a considerable
and escalating cybersecurity threat. Adversarial patches
are intricately designed perturbations, whether physical
objects or digital modifications, crafted with precision to
deceive AI vision systems. These deceptive alterations can
manipulate the system&#x27;s perception and decision-making
processes, resulting in erroneous classifications. Such
manipulation can empower malicious actors to bypass
established security measures, take control of autonomous
operations, or elude detection mechanisms, potentially
leading to catastrophic consequences.

This research carefully examines the urgent necessity for
adversarial patch detection as an essential component of a
comprehensive defensive strategy within the cybersecurity
landscape. It explores the increasing sophistication of
current adversarial attack methodologies, which often
exploit subtle vulnerabilities in AI algorithms with
alarming effectiveness. Moreover, the study investigates
the capabilities of emerging detection frameworks that aim
to identify, analyze, and mitigate these sophisticated
threats. By exploring the dynamic relationship between
advancing adversarial tactics and the evolving defense
mechanisms, this work seeks to illuminate strategies to
bolster the resilience of AI systems against these
insidious attacks, thereby enhancing the safety and
reliability of critical infrastructure in a rapidly
evolving digital landscape.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="detecting physical adversarial patch attacks with object detectors damone washington, rebecca caldwell deep learning-based object detection technologies, such as yolov5 and faster r-cnn, are being increasingly applied in safety-critical areas, including self-driving cars, surveillance systems, and smart transportation infrastructure. although these models show remarkable performance under standard conditions, they are vulnerable to physical adversarial patch attacks. these attacks involve the careful placement of specifically designed printed perturbations in a scene to provoke misclassification or to obscure objects. in contrast to digital attacks that take place in controlled settings, physical adversarial patches operate under real-world conditions, where variables such as changing light, distance, angle, and occlusion can greatly influence their effectiveness, making them a significant danger. this study explores detection-based defense mechanisms designed to identify physical adversarial patch attacks using object detectors. we assess various methods, including confidence-score analysis, monitoring of bounding-box instability, feature-distribution anomaly detection, and ensemble-based detection strategies. to simulate realistic deployment scenarios, researchers collected a controlled dataset of both clean and patched objects under various environmental conditions. the detection performance is evaluated using precision, recall, f1-score, mean average precision (map), and inference latency. early investigation of research studies suggests that the use of ensemble detection, along with tracking confidence distributions, significantly improves the detection rates of adversarial patch attacks while keeping performance near real-time levels. this research focuses on identifying, rather than stopping, physical adversarial patch attacks using object detection-based defense strategies. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_80.pdf">Detecting Physical Adversarial Patch Attacks with Object
Detectors</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Damone Washington, Rebecca Caldwell</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Deep learning-based object detection technologies, such as
YOLOv5 and Faster R-CNN, are being increasingly applied in
safety-critical areas, including self-driving cars,
surveillance systems, and smart transportation
infrastructure. Although these models show remarkable
performance under standard conditions, they are vulnerable
to physical adversarial patch attacks. These attacks
involve the careful placement of specifically designed
printed perturbations in a scene to provoke
misclassification or to obscure objects. In contrast to
digital attacks that take place in controlled settings,
physical adversarial patches operate under real-world
conditions, where variables such as changing light,
distance, angle, and occlusion can greatly influence their
effectiveness, making them a significant danger.
This study explores detection-based defense mechanisms
designed to identify physical adversarial patch attacks
using object detectors. We assess various methods,
including confidence-score analysis, monitoring of
bounding-box instability, feature-distribution anomaly
detection, and ensemble-based detection strategies. To
simulate realistic deployment scenarios, researchers
collected a controlled dataset of both clean and patched
objects under various environmental conditions. The
detection performance is evaluated using precision, recall,
F1-score, mean Average Precision (mAP), and inference
latency.
Early investigation of research studies suggests that the
use of ensemble detection, along with tracking confidence
distributions, significantly improves the detection rates
of adversarial patch attacks while keeping performance near
real-time levels. This research focuses on identifying,
rather than stopping, physical adversarial patch attacks
using object detection-based defense strategies.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="structural augmentation for conspiracy detection: a modernbert approach to psycomark 2026 subtask 2 lashaun baddol, saurav aryal, lashaun baddol the psycomark 2026 shared task emphasizes modeling the psycholinguistic structure underlying conspiracy belief expression rather than relying solely on topical cues. in this work, we address subtask 2, which requires classifying reddit comments as conspiracy-related or non-conspiracy-related across diverse domains. we implement a syntactically augmented transformer-based classifier using modernbert-base. to introduce lightweight structural information aligned with psycomark’s theoretical framing, we extract part-of-speech (pos) tags using spacy and concatenate the resulting syntactic sequence with the original comment text via a separator token. this approach allows the model to jointly encode lexical semantics and shallow grammatical structure without architectural modification. the model is fine-tuned for binary classification using cross-entropy loss, with early stopping applied to reduce overfitting. preliminary experiments on the official development split yield a macro-averaged f1 score of 0.46. while performance remains modest, these results establish a functional baseline for structurally augmented classification and provide initial insight into the contribution of shallow syntactic signals for conspiracy detection in topic-diverse online discussions. this work contributes an empirically grounded starting point for exploring psycholinguistically informed transformer models within the psycomark framework. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_81.pdf">Structural Augmentation for Conspiracy Detection: A
ModernBERT Approach to PsyCoMark 2026 Subtask 2</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Lashaun Baddol, Saurav Aryal, Lashaun Baddol</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">The PsyCoMark 2026 shared task emphasizes modeling the
psycholinguistic structure underlying conspiracy belief
expression rather than relying solely on topical cues. In
this work, we address Subtask 2, which requires classifying
Reddit comments as conspiracy-related or
non-conspiracy-related across diverse domains.

We implement a syntactically augmented transformer-based
classifier using ModernBERT-base. To introduce lightweight
structural information aligned with PsyCoMark’s theoretical
framing, we extract Part-of-Speech (POS) tags using spaCy
and concatenate the resulting syntactic sequence with the
original comment text via a separator token. This approach
allows the model to jointly encode lexical semantics and
shallow grammatical structure without architectural
modification. The model is fine-tuned for binary
classification using cross-entropy loss, with early
stopping applied to reduce overfitting.

Preliminary experiments on the official development split
yield a macro-averaged F1 score of 0.46. While performance
remains modest, these results establish a functional
baseline for structurally augmented classification and
provide initial insight into the contribution of shallow
syntactic signals for conspiracy detection in topic-diverse
online discussions.

This work contributes an empirically grounded starting
point for exploring psycholinguistically informed
transformer models within the PsyCoMark framework.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="evaluating perceptions of naturalness in ai-generated speech ogechi anyamele, saurav aryal, gloria washington advances in neural text-to-speech technologies have allowed for realistic voice cloning, however, determining how “natural” synthetic voices are remains a challenge. as voice cloning becomes more integrated into applications such as accessibility systems, entertainment platforms, virtual assistants, and more, the quality of synthetic speech becomes increasingly significant. subtle differences can shape listeners&#x27; attitudes towards usability, reduce trust, and affect overall user experience. therefore, identifying factors that contribute to human-like speech and establishing reliable methods to evaluate perceived naturalness is essential in advancing speech synthesis systems. this study investigates the relationship between training data quantity and perceived human-likeness in cloned voices using a neural voice cloning pipeline based on coqui xtts. an end-to-end voice cloning system was implemented, with voice models trained on speech samples of varying lengths. synthetic speech outputs were generated from each model and evaluated through a qualitative listening study. the generated voice samples were assessed by three human evaluators: self, familiar, and unfamiliar listeners. evaluators rated each sample on a five-point likert scale for perceived naturalness. ratings were compiled into a structured dataset for comparative analysis. additionally, different approaches for evaluating speech naturalness were explored to inform the study design. thus far, the end-to-end system has been implemented, models have been trained under varying data conditions, and listening evaluations have been conducted to support ongoing analysis. together, these components establish a systematic framework for examining how training data quantity relates to perceived naturalness in synthetic speech, offering a foundation for further refinement in voice cloning applications. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_82.pdf">Evaluating Perceptions of Naturalness in AI-Generated Speech</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Ogechi Anyamele, Saurav Aryal, Gloria Washington</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Advances in neural text-to-speech technologies have allowed
for realistic voice cloning, however, determining how
“natural” synthetic voices are remains a challenge. As
voice cloning becomes more integrated into applications
such as accessibility systems, entertainment platforms,
virtual assistants, and more, the quality of synthetic
speech becomes increasingly significant. Subtle differences
can shape listeners&#x27; attitudes towards usability, reduce
trust, and affect overall user experience. Therefore,
identifying factors that contribute to human-like speech
and establishing reliable methods to evaluate perceived
naturalness is essential in advancing speech synthesis
systems.
This study investigates the relationship between training
data quantity and perceived human-likeness in cloned voices
using a neural voice cloning pipeline based on Coqui XTTS.
An end-to-end voice cloning system was implemented, with
voice models trained on speech samples of varying lengths.
Synthetic speech outputs were generated from each model and
evaluated through a qualitative listening study. The
generated voice samples were assessed by three human
evaluators: self, familiar, and unfamiliar listeners.
Evaluators rated each sample on a five-point Likert scale
for perceived naturalness. Ratings were compiled into a
structured dataset for comparative analysis. Additionally,
different approaches for evaluating speech naturalness were
explored to inform the study design.
Thus far, the end-to-end system has been implemented,
models have been trained under varying data conditions, and
listening evaluations have been conducted to support
ongoing analysis. Together, these components establish a
systematic framework for examining how training data
quantity relates to perceived naturalness in synthetic
speech, offering a foundation for further refinement in
voice cloning applications.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="cross-silo federated learning for radiomics anthony tucker, saurav keshari aryal radiomics allows for the extraction of features from medical images for predictive modeling, but due to data privacy regulations, training models on multi-institutional datasets is not feasible. we propose a cross-silo federated learning framework that allows hospitals to jointly train radiomics models without sharing patient data. our solution utilizes the flower framework and the radmlbench benchmark (50+ radiomics datasets) to create a multi-hospital federated learning setting. each hospital is given unique datasets, as seen in real-world settings. we handle feature heterogeneity by using intersection-based feature alignment, making the model compatible across hospitals. the framework utilizes a four-layer neural network architecture that is trained locally at each hospital. the central server combines the model parameters using federated averaging (fedavg), weighted by the number of samples. we compare the federated learning method with a centralized approach that trains on aggregated data using accuracy as a metric. although the centralized approach has the advantage of direct access to all the data, the federated approach is able to attain similar results while preserving the privacy of the data, thus proving that collaborative learning can come close to the centralized approach without breaching the privacy constraints. the framework is applied to brain-related disorders (gliomas and glioblastomas) using mri images, thus illustrating how different institutions can work together to collaboratively enhance the performance of the model while being hipaa compliant. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_84.pdf">Cross-Silo Federated Learning for Radiomics</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Anthony Tucker, Saurav Keshari Aryal</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Radiomics allows for the extraction of features from
medical images for predictive modeling, but due to data
privacy regulations, training models on multi-institutional
datasets is not feasible. We propose a cross-silo federated
learning framework that allows hospitals to jointly train
radiomics models without sharing patient data.
Our solution utilizes the Flower framework and the
radMLBench benchmark (50+ radiomics datasets) to create a
multi-hospital federated learning setting. Each hospital is
given unique datasets, as seen in real-world settings. We
handle feature heterogeneity by using intersection-based
feature alignment, making the model compatible across
hospitals.
The framework utilizes a four-layer neural network
architecture that is trained locally at each hospital. The
central server combines the model parameters using
Federated Averaging (FedAvg), weighted by the number of
samples. We compare the federated learning method with a
centralized approach that trains on aggregated data using
accuracy as a metric. Although the centralized approach has
the advantage of direct access to all the data, the
federated approach is able to attain similar results while
preserving the privacy of the data, thus proving that
collaborative learning can come close to the centralized
approach without breaching the privacy constraints. The
framework is applied to brain-related disorders (gliomas
and glioblastomas) using MRI images, thus illustrating how
different institutions can work together to collaboratively
enhance the performance of the model while being HIPAA
compliant.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="comparative analysis of adversarial patch types and their distinct cybersecurity risks in computer vision systems brennen saine adversarial patches pose a growing threat to artificial intelligence systems that rely on computer vision for automated decision-making. this research examines how different types of adversarial patches affect ai models in distinct ways and analyzes the unique cybersecurity risks associated with each. the study focuses on universal, targeted, untargeted, and physically robust patches and evaluates their influence on model accuracy, misclassification behavior, environmental resilience, and attack scalability. by comparing these patch types, the poster identifies how their design determines the level of disruption they cause and the environments in which they are most effective. the findings indicate that universal patches present large-scale operational risks due to their transferability across multiple systems, while targeted patches create significant threats to biometric authentication and identity-based security. untargeted patches primarily impact system reliability and decision integrity, whereas physically robust patches introduce the most severe real-world dangers by maintaining effectiveness under varying physical conditions. these differences demonstrate that adversarial patch attacks are not a single, uniform threat but a collection of vulnerabilities that require specialized defensive strategies. understanding how each patch type affects ai behavior and security is essential for developing resilient models and protecting ai-driven technologies in enterprise, public safety, and critical infrastructure environments. poster student - undergraduate poster">
  <h4>Comparative Analysis of Adversarial Patch Types and Their
Distinct Cybersecurity Risks in Computer Vision Systems</h4>
  <div class="paper-meta"><strong>Authors:</strong> Brennen Saine</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Adversarial patches pose a growing threat to artificial
intelligence systems that rely on computer vision for
automated decision-making. This research examines how
different types of adversarial patches affect AI models in
distinct ways and analyzes the unique cybersecurity risks
associated with each. The study focuses on universal,
targeted, untargeted, and physically robust patches and
evaluates their influence on model accuracy,
misclassification behavior, environmental resilience, and
attack scalability. By comparing these patch types, the
poster identifies how their design determines the level of
disruption they cause and the environments in which they
are most effective. The findings indicate that universal
patches present large-scale operational risks due to their
transferability across multiple systems, while targeted
patches create significant threats to biometric
authentication and identity-based security. Untargeted
patches primarily impact system reliability and decision
integrity, whereas physically robust patches introduce the
most severe real-world dangers by maintaining effectiveness
under varying physical conditions. These differences
demonstrate that adversarial patch attacks are not a
single, uniform threat but a collection of vulnerabilities
that require specialized defensive strategies.
Understanding how each patch type affects AI behavior and
security is essential for developing resilient models and
protecting AI-driven technologies in enterprise, public
safety, and critical infrastructure environments.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="ai4pc-howard university at semeval-2026 task 9: multilingual polarization detection via large language model inference surangana aryal, saurav keshari aryal, soluchi fidelibeab this paper describes the polarnlp system submitted to semeval-2026 task 9, subtask 1, which focuses on detecting political polarization in multilingual text. the task spans 22 typologically diverse languages and poses challenges related to domain shift, class imbalance, and cross-lingual generalization. we explored two modeling strategies: (i) a weakly supervised teacher–student approach that uses a large language model (llm) to generate pseudolabels for training a multilingual classifier, and (ii) direct llm-based inference augmented with language-agnostic stylistic features. while the teacher–student approach achieved reasonable in-distribution performance, it failed to generalize to the heldout test set, collapsing toward the majority class. consequently, our final submission relies on direct llm inference. we present a detailed analysis of both approaches, highlighting the limitations of weak supervision for polarization detection and the relative robustness of direct llm reasoning in multilingual settings. poster student - undergraduate poster">
  <h4><a href="sorted_papers/Poster/Student - Undergraduate/ADMI_2026_paper_89.pdf">AI4PC-Howard University at SemEval-2026 Task 9:
Multilingual Polarization Detection via Large Language
Model Inference</a></h4>
  <div class="paper-meta"><strong>Authors:</strong> Surangana Aryal, Saurav Keshari Aryal, Soluchi Fidelibeab</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">accept poster?</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">This paper describes the PolarNLP system submitted to
SemEval-2026 Task 9, Subtask 1, which focuses on detecting
political polarization in multilingual text. The task spans
22 typologically diverse languages and poses challenges
related to domain shift, class imbalance, and cross-lingual
generalization. We explored two modeling strategies: (i) a
weakly supervised teacher–student approach that uses a
large language model (LLM) to generate pseudolabels for
training a multilingual classifier, and (ii) direct
LLM-based inference augmented with language-agnostic
stylistic features. While the teacher–student approach
achieved reasonable in-distribution performance, it failed
to generalize to the heldout test set, collapsing toward
the majority class. Consequently, our final submission
relies on direct LLM inference. We present a detailed
analysis of both approaches, highlighting the limitations
of weak supervision for polarization detection and the
relative robustness of direct LLM reasoning in multilingual
settings.</div>
  </details>
</article>

<article class="paper-card submission-card" data-section="Poster" data-authorcat="Student - Undergraduate" data-search="transformer-based suicide detection on reddit with sentiment masking brionna nunn, soo-yeon ji suicide continues to be an ongoing worldwide public health concern, and social media sites such as reddit provide essential forums for people to communicate their psychological suffering. this research study uses a labeled reddit dataset to develop a transformer-based technique for suicide risk detection. we build a base classification model to differentiate suicidal from non-suicidal posts, utilizing the contextual representation capabilities of pretrained transformer patterns. we introduce three masking strategies during training: (1) masking positive words, (2) masking negative words, and (3) masking both positive and negative phrases to examine the impact of sentiment-driven linguistic signals. the purpose of these masking techniques is to examine the ways in which sensitive lexical elements influence decision limitations and model performance. we test the reliability of contextual embeddings and determine whether the transformer predominantly relies on deeper semantic structures or on explicit emotive terminology by selectively eliminating sentiment signals. the research results use common assessment measures such as accuracy, precision, recall, and f1-score to compare the base model with its masked versions. our results show how lexical masking can be used as an interpretability and analysis method, shedding light on the role of sentiment polarity in suicide detection tasks. this study contributes to the development of more dependable and comprehensible ai algorithms for the early identification of suicide risk in social media platforms. poster student - undergraduate poster">
  <h4>Transformer-Based Suicide Detection on Reddit with
Sentiment Masking</h4>
  <div class="paper-meta"><strong>Authors:</strong> Brionna Nunn, Soo-Yeon Ji</div>
  <div class="paper-meta"><strong>Submission type:</strong> Poster</div>
  <div class="badges">
    <span class="badge poster">Poster</span>
    <span class="badge">Student - Undergraduate</span>
    <span class="badge">Poster</span>
    <span class="badge">ACCEPT POSTER</span>
  </div>
  <details>
    <summary>Abstract</summary>
    <div class="abstract">Suicide continues to be an ongoing worldwide public health
concern, and social media sites such as Reddit provide
essential forums for people to communicate their
psychological suffering. This research study uses a labeled
Reddit dataset to develop a Transformer-based technique for
suicide risk detection. We build a base classification
model to differentiate suicidal from non-suicidal posts,
utilizing the contextual representation capabilities of
pretrained Transformer patterns. We introduce three masking
strategies during training: (1) masking positive words, (2)
masking negative words, and (3) masking both positive and
negative phrases to examine the impact of sentiment-driven
linguistic signals. The purpose of these masking techniques
is to examine the ways in which sensitive lexical elements
influence decision limitations and model performance. We
test the reliability of contextual embeddings and determine
whether the Transformer predominantly relies on deeper
semantic structures or on explicit emotive terminology by
selectively eliminating sentiment signals. The research
results use common assessment measures such as accuracy,
precision, recall, and F1-score to compare the base model
with its masked versions. Our results show how lexical
masking can be used as an interpretability and analysis
method, shedding light on the role of sentiment polarity in
suicide detection tasks. This study contributes to the
development of more dependable and comprehensible AI
algorithms for the early identification of suicide risk in
social media platforms.</div>
  </details>
</article>

</div>
</div>

</div>


<script>
(function () {
  const cards = Array.from(document.querySelectorAll('.submission-card'));
  const buttons = Array.from(document.querySelectorAll('.filter-btn'));
  const tagTriggers = Array.from(document.querySelectorAll('.tag-trigger'));
  const searchInput = document.getElementById('searchInput');
  const resultsCount = document.getElementById('resultsCount');
  let activeFilter = 'All';

  function normalize(value) {
    return (value || '').toLowerCase();
  }

  function applyFilters() {
    const q = normalize(searchInput.value);
    let shown = 0;

    cards.forEach(card => {
      const section = card.dataset.section;
      const authorcat = card.dataset.authorcat;
      const search = normalize(card.dataset.search);

      const matchesText = !q || search.includes(q);
      const matchesFilter =
        activeFilter === 'All' ||
        section === activeFilter ||
        authorcat === activeFilter;

      const visible = matchesText && matchesFilter;
      card.classList.toggle('hidden-by-filter', !visible);
      if (visible) shown += 1;
    });

    resultsCount.textContent = shown;
  }

  function setActiveFilter(value) {
    activeFilter = value;
    buttons.forEach(btn => btn.classList.toggle('active', btn.dataset.filter === value));
    applyFilters();
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => setActiveFilter(btn.dataset.filter));
  });

  tagTriggers.forEach(link => {
    link.addEventListener('click', () => {
      setActiveFilter(link.dataset.filter);
      window.scrollTo({ top: document.querySelector('.filter-panel').offsetTop - 12, behavior: 'smooth' });
    });
  });

  searchInput.addEventListener('input', applyFilters);
  applyFilters();
})();
</script>

</div>
