<script>
  import MessageItem from "./MessageItem.svelte";
  export let messages = [];

</script>

<div class="h-full w-full py-4 px-6 flex flex-col gap-2 overflow-y-auto">

{#each messages as message, idx}
  <MessageItem text={message.text ?? ""} isUser={message.isUser} />
{/each}

</div>