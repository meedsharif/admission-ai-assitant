<script>

  import Header from "../components/Header.svelte";
  import MessageInput from "../components/MessageInput.svelte";
  import Messages from "../components/Messages.svelte";

  const api = import.meta.env.VITE_API_ENDPOINT;
  let messages = [];
  let fetchingResponse = false;

  async function handleSubmit(e) {
    const text = e.detail;
    
    messages = [
      ...messages,
      {
        text,
        isUser: true,
      },
    ];
    
    fetchingResponse = true;
    
    const res = await fetch(api + "/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question: text,
      }),
    });
    
    const data = await res.json();
    
    
    messages = [
      ...messages,
      {
        text: data.response,
        isUser: false,
      },
    ];

    fetchingResponse = false;

  }

</script>

<div class="w-2/5 h-[40rem] bg-white rounded-lg shadow-xl overflow-hidden flex flex-col border border-black border-opacity-20">
  <Header />

  <Messages {messages} />

  <MessageInput 
    {fetchingResponse}
    on:submit={handleSubmit}
  />
</div>
