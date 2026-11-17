from langchain_openai import ChatOpenAI

# 1. Initialize the LLM
# Note: temperature=0.7 introduces creativity/randomness across runs.
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 2. Define the prompt with pinned format (numbered, one line each, no preamble)
prompt = (
    "Give me exactly 5 healthy breakfast ideas. "
    "Format them as numbered items (1. to 5.), one line each, with no preamble or extra text."
)

# 3. Invoke the model
reply = llm.invoke(prompt)

# --- THE LESSON: MESSAGE OBJECT VS. CONTENT ---
print("=== 1. What invoke() hands you directly (The whole message object) ===")
print(reply)
print("\n" + "="*50 + "\n")

print("=== 2. What you actually want (Just the text content) ===")
print(reply.content)