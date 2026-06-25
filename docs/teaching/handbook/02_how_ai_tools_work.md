# Chapter 2 — How AI Tools Work

> Before we talk about tools and workflows, you need a clear picture of what an AI coding tool actually *is*. Most confusion comes from having the wrong picture in your head.

---

## The Simple Version

An AI coding tool has two main parts:

1. **The model** — the "brain." This is the AI itself. It reads text and writes text. That is all it does.
2. **The harness** — the "body." This is the software around the model. It gives the model tools, files, and a way to talk to you.

The model is smart but cannot do anything on its own. The harness is what turns the model into something useful.

---

## The Model: The Brain

A **model** (also called an LLM, or Large Language Model) is a computer program that takes text in and gives text back. You give it a question, it gives you an answer. You give it code, it explains the code. You give it a bug, it suggests a fix.

Here is the important part: **the model can only write text.** It cannot read a file. It cannot run a command. It cannot search the web. It can only read what you paste into it and write back a response.

Two more things to know about models:

1. **They have no memory between conversations.** Every time you start a new chat, the model starts fresh. It does not remember yesterday's conversation. Anything you want it to know has to be in *this* conversation.

2. **They are confident even when they are wrong.** A model can write something that sounds very sure but is actually incorrect. This is called **hallucination**, and it is why you always need to check the AI's work. (More on this in [Chapter 11: Code of Conduct](11_code_of_conduct.md).)

---

## The Harness: The Body

A **harness** is the software that wraps the model and turns it into a usable tool. Think of it this way:

- The **model** is the engine.
- The **harness** is the whole car — steering wheel, brakes, dashboard, seatbelt.

opencode, Cursor, Claude Code, and Aider are all **harnesses**. They use different models underneath (Claude, GPT, Gemini, Llama), but they all do the same fundamental job: take a smart-but-limited model and give it the parts it needs to actually work on your code.

The harness gives the model:

- **Tools** — read a file, edit a file, run a shell command, search the web.
- **A chat window** — so you can talk to it.
- **Safety checks** — so it does not do something dangerous without asking you.
- **Memory within a session** — so it remembers what you said earlier in the same conversation.

When you pick a tool like opencode or Cursor, you are picking a **harness**, not a model. Most harnesses let you swap the model underneath. The harness is what shapes your experience.

---

## The Agentic Loop

Here is the thing that makes modern AI tools feel different from a chatbot. It is called the **agentic loop**:

```
1. Observe   - read the task, look at relevant files
2. Reason    - decide what to do next
3. Act       - call a tool: edit a file, run a command
4. Observe   - read the result of the action
5. Repeat    - until the task is done or the agent gets stuck
```

Without tools, the loop cannot *act*. It can only write text, and you have to do everything it suggests yourself. With tools, the loop can run on its own for many steps before needing your help.

Here is what this looks like in real life:

1. You say: "Fix the bug in login.ts."
2. The AI reads `login.ts` to see what is there.
3. It figures out the bug.
4. It edits the file.
5. It runs the tests to see if they pass now.
6. If they fail, it reads the error, fixes the code again, and reruns the tests.
7. When the tests pass, it stops and tells you.

That whole sequence is the agentic loop in action. The AI is not just answering a question — it is *doing* something, step by step, until the job is done.

---

## Why Tools Matter More Than Prompting

A common beginner mistake is to focus on writing the perfect prompt. But the prompt is only half the story. The **tools** the AI has access to matter just as much, often more.

Here is why: a mediocre prompt with good tools (file search, run tests, edit code) will outperform a brilliant prompt with no tools. Why? Because with tools, the AI can **check its own work**. It can read the file, make a change, run the test, see if it passes, and fix it if not. Without tools, it just guesses and hopes.

The professional shift is this: **stop trying to write the perfect prompt, and start making sure the AI has the right tools.** Then almost any reasonable prompt works.

---

## The Big Picture

- A **model** is the brain — text in, text out.
- A **harness** is the body — tools, files, safety, chat.
- The **agentic loop** is what makes the tool feel alive — observe, reason, act, repeat.
- **Tools** are what let the AI actually do things, not just talk.

Now that you have the picture, the next chapter explains the four layers of an AI coding tool in more detail.

Continue to [Chapter 3 — The Stack: Model, Harness, Client, Server](03_the_stack.md).
