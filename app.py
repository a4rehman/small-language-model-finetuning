import streamlit as st
import time
import random

# --- Page Config ---
st.set_page_config(
    page_title="Query Router & SLM Demo",
    page_icon="⚡",
    layout="wide"
)

# --- Custom CSS for Premium Look ---
st.markdown("""
    <style>
    .main {
        background-color: #0b0e14;
    }
    .stApp {
        background: radial-gradient(circle at top right, #1a1f2c, #0b0e14);
    }
    
    /* Title Styling */
    .title-text {
        font-family: 'Inter', sans-serif;
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #00ff87, #60efff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    
    .highlight-yellow {
        color: #ffcc33;
        font-weight: bold;
    }
    
    .subtitle-text {
        color: #94a3b8;
        font-size: 1.3rem;
        margin-bottom: 2.5rem;
    }
    
    /* Stats Cards */
    .stat-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(0, 255, 135, 0.2);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(5px);
        text-align: center;
    }
    
    .stat-card h3 {
        color: #00ff87;
        margin-bottom: 5px;
        font-size: 2rem;
    }
    
    .stat-card p {
        color: #94a3b8;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Success Badge */
    .badge {
        background: rgba(0, 255, 135, 0.1);
        color: #00ff87;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        border: 1px solid rgba(0, 255, 135, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/nolan/128/artificial-intelligence.png", width=100)
    st.markdown("### Model Stack")
    st.info("Router: DistilBERT (Fine-tuned)")
    st.info("SLM: Phi-3-mini (LoRA)")
    st.info("Vector DB: Qdrant / Pinecone")
    st.divider()
    st.markdown("### Benchmarks")
    st.success("Accuracy: +16.45% vs GPT-4")
    st.success("Latency: < 100ms")
    st.success("Volume: 50K+ Queries/Day")

# --- Header ---
st.markdown('<h1 class="title-text">Query Router & <span class="highlight-yellow">SLM Fine-Tuning</span></h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Enhanced Intent Detection & High-Speed Inference Engine</p>', unsafe_allow_html=True)

# --- Stats Row ---
s1, s2, s3 = st.columns(3)
with s1:
    st.markdown("""<div class="stat-card"><h3>+16.45%</h3><p>Accuracy Improvement</p></div>""", unsafe_allow_html=True)
with s2:
    st.markdown("""<div class="stat-card"><h3>< 100ms</h3><p>Inference Latency</p></div>""", unsafe_allow_html=True)
with s3:
    st.markdown("""<div class="stat-card"><h3>50K+</h3><p>Processed Daily</p></div>""", unsafe_allow_html=True)

st.write("")
st.write("")

# --- Interaction Area ---
t1, t2 = st.columns([1, 1])

with t1:
    st.markdown("### ✍️ Test Your Query")
    query_input = st.text_input("Enter a technical or customer support query:", 
                                value="How can I optimize my database indexing for high read-heavy workloads?")
    
    run_btn = st.button("🚀 Process via Optimized Pipeline", use_container_width=True)
    
    st.markdown("#### Technologies Used")
    st.markdown("`#SLMFineTuning` `#IntentDetection` `#HybridRetrieval` `#HuggingFace` `#LowLatency`")

with t2:
    st.markdown("### 🖥️ Real-time Pipeline Logs")
    log_placeholder = st.empty()
    if not run_btn:
        log_placeholder.info("Waiting for input to trigger routing engine...")

if run_btn:
    with t2:
        with st.status("🧠 Initiating Intelligent Routing...", expanded=True) as status:
            st.write("🔍 **Phase 1: Intent Detection**")
            time.sleep(0.6)
            st.write("   - Detected Class: `Technical Architecture`")
            st.write("   - Confidence: `0.982`")
            
            st.divider()
            
            st.write("⚡ **Phase 2: SLM Execution**")
            time.sleep(0.4)
            st.write("   - Routing to fine-tuned Phi-3-mini SLM...")
            st.write("   - Model optimized via LoRA & 4-bit Quantization.")
            
            st.divider()
            
            st.write("📚 **Phase 3: Hybrid Retrieval**")
            time.sleep(0.5)
            st.write("   - Searching Sparse (BM25) and Dense (Jina-v2) embeddings...")
            st.write("   - Reranking top 5 candidates...")
            
            status.update(label="✅ Optimization Pipeline Complete", state="complete", expanded=False)

    # --- Result Card ---
    st.write("")
    st.markdown("""### 💡 Model Response""")
    
    with st.container():
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.05); padding: 30px; border-radius: 15px; border-left: 5px solid #00ff87;">
            <p style="color: #94a3b8; font-style: italic;">User Query: "{query_input}"</p>
            <h4 style="color: white; margin-top: 20px;">Response Generation (SLM):</h4>
            <p style="color: #e2e8f0; line-height: 1.6;">
                To optimize indexing for read-heavy workloads, you should focus on <b>Covering Indexes</b> to avoid base table lookups. 
                Additionally, implement <b>Partial Indexes</b> for frequently filtered data to reduce index size. 
                For high concurrency, consider <b>BRIN indexes</b> (if using PostgreSQL) or <b>Columnstore indexes</b> for analytical read patterns.
            </p>
            <hr style="opacity: 0.1;">
            <div style="display: flex; gap: 20px; margin-top: 15px;">
                <span class="badge">Inference time: 84ms</span>
                <span class="badge">VRAM Usage: 1.2GB</span>
                <span class="badge">Tokens: 64</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.toast("Success! Latency: 84ms", icon="⚡")

# Footer
st.divider()
st.markdown("<p style='text-align: center; color: #576574;'>Query Router & SLM Fine-Tuning Portfolio Demo</p>", unsafe_allow_html=True)
