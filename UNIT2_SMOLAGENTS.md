# Unit 2: smolagents with a local model

## Setup
- **Library:** smolagents (free, open source, from Hugging Face)
- **Model:** `Qwen/Qwen2.5-Coder-3B-Instruct`, run locally in Google Colab on a free T4 GPU
- **Why not the hosted model:** the course's default, `InferenceClientModel`, now requires paid credits and returned 403 billing errors.
- **Why 3B:** the 1.5B model couldn't reliably pick tools or format answers. The 32B model used in the course doesn't fit on a free GPU.

## Tasks
1. **Restaurant menu:** a `CodeAgent` with a custom `suggest_menu(occasion)` tool. Input: `formal`. Expected output: `3-course dinner with wine and dessert.`
2. **Preparation time:** a `CodeAgent` with a `party_ready_time(task_minutes)` tool. Input: `30,60,45,45`. Expected output: total of 180 minutes and a ready time.
3. **Song search:** a `CodeAgent` with `DuckDuckGoSearchTool`. Query: `best music for a Batman party`. Expected output: search results.

## Results
- Menu task: 3-course dinner with wine and dessert. (Called the tool correctly.)
- Time task: not completed as designed. The agent wrote its own datetime code and returned `2026-11-05 06:29:51`. It did not call `party_ready_time`.
- Song task: returned a list of web links (Spotify, YouTube, Reddit). The agent used `web_search`, and several results were not party-related.

## Errors I hit and how I fixed them
- **403 billing error** from the hosted model: switched to a local model.
- **`Final answer: None`**: the model didn't pass the result to `final_answer()`. Fixed by naming the tool and output format in the prompt.
- **Model wrote its own menu or function** instead of calling my tool: named the tool and argument in the prompt. The model still sometimes ignored this.
- **`Import of requests is not allowed`**: the model wrote its own web code. I didn't allow `requests`, so the sandbox blocked it.
- **Backticks inside the code block** caused `SyntaxError`: fixed by asking for `<code></code>` tags with no backticks.
- **`NameError: name 'datetime' is not defined`**: tools run in the agent's sandbox, which doesn't see notebook imports. Fixed by importing inside the function.
- **`NameError: name 'tool' is not defined`**: I ran a cell out of order. Fixed by running the setup cell first.
- **`AttributeError: 'int' object has no attribute 'split'`**: the model passed a number instead of text. Fixed by converting the input with `str()`.
- **`TypeError: unsupported type for timedelta minutes component: str`**: the model passed the wrong type into the time calculation.
- **`InterpreterError: Cannot assign to name 'party_ready_time'`**: the model used a variable with the same name as the tool, which overwrote it.

## Limits I observed
- The 3B model still sometimes writes its own code instead of calling the given tool.
- Its formatting is unreliable, so some runs hit the step limit.
- The time task didn't use the tool, so its result isn't verified against the 180-minute total.
- Hosted models would likely do better, but they need credits.
