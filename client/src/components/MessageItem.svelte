<script>

  export let text = "";
  export let isUser = false;


</script>

<div class="">
  <div class="flex flex-col items-end">
    <div class="bg-blue-500 text-white rounded-lg p-2 self-end" class:robot={!isUser}>
      {text}
    </div>
  </div>
</div>

<style>

  .robot {
    @apply self-start bg-cyan-500;
  }

</style>