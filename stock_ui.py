import streamlit as st
import asyncio
from io import StringIO
import sys
from contextlib import redirect_stdout
from stock_recommender_system import run_agent


st.set_page_config(
    page_title="Multi-Agent Stock Research Assistant",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Multi-Agent Stock Research Assistant (CSE)")
st.markdown("""
Welcome to the **AI and MCP Powered Stock Research System** 

Enter your research query below and watch multiple AI agents collaborate 
to find the best trading opportunities on the **Colombo Stock Exchange (CSE)**.
""")


with st.sidebar:
    st.header("⚙️ Configuration")
    st.markdown("""
    **Agents Used:**
    - 🧩 Stock Finder Agent  
    - 📊 Market Data Agent  
    - 📰 News Analyst Agent  
    - 💰 Price Recommender Agent  
    """)


query = st.text_area("💬 Enter your query:", "Give me good stock recommendation from CSE")

if st.button("🚀 Run Stock Analysis", use_container_width=True):
    st.markdown("### 🧠 Agent Collaboration in Progress...")
    output_placeholder = st.empty()

    buffer = StringIO()

    async def capture_output():
        with redirect_stdout(buffer):
            await run_agent(query)
        return buffer.getvalue()

    try:
        with st.spinner("Running multi-agent workflow... please wait ⏳"):
            output = asyncio.run(capture_output())

        st.success("✅ Analysis Completed Successfully!")
        st.markdown("### 📊 Detailed Agent Logs")
        st.text_area("Agent Process Logs", output, height=400)

        # Extract and highlight final recommendations (simple heuristic)
        if "Recommendation" in output:
            st.markdown("### 💡 Final Stock Recommendations")
            recommendations = []
            lines = output.split("\n")
            for line in lines:
                if any(word in line for word in ["BUY", "SELL", "HOLD", "Target Price"]):
                    recommendations.append(line.strip())

            if recommendations:
                st.code("\n".join(recommendations), language="markdown")
            else:
                st.info("No explicit recommendations found in output.")
        else:
            st.warning("No recommendations detected in the output.")

    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.exception(e)
