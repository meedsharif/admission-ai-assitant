
<script>
  import { createEventDispatcher, tick } from "svelte";

  const dispatch =   createEventDispatcher();

  let inputValue = "";
  let input;
  export let fetchingResponse = true;

  $: if(fetchingResponse === false) {
    focusInput()
  }

  async function focusInput() {
    await tick();
    input?.focus();
  }

  function handleKeyPress(e) {
    if (e.key === "Enter") {
      submitMEssage();
    }
  }

  function submitMEssage() {
    dispatch("submit", inputValue);
    inputValue = "";
  }

</script>

<div class="w-full mt-auto bg-gray-100 py-2 px-6 flex gap-4 border-t border-black border-opacity-10">
  <input class="flex-grow bg-white rounded  border border-black border-opacity-30 py-2 p-4 disabled:bg-gray-200 disabled:cursor-not-allowed" disabled={fetchingResponse} placeholder="Ask a question..." type="text" 
  on:keypress={handleKeyPress}
  bind:this={input}
  bind:value={inputValue}>
  <button class="bg-blue-500 px-6 rounded text-white font-semibold disabled:bg-gray-400 disabled:cursor-not-allowed" on:click|preventDefault={submitMEssage} disabled={fetchingResponse}>Ask</button>
</div>