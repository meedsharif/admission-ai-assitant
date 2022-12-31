<script>
  import "../app.postcss";
</script>

<div class="w-screen h-screen bg-gradient-to-r from-cyan-500 to-blue-500 flex items-center justify-center">
  <slot />
</div>


<style>

:global(::-webkit-scrollbar-track) {
		/* -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2); */
		/* border-radius: 10px; */
		background-color: #e2e5eb;
	}

	:global(::-webkit-scrollbar) {
		height: 6px;
		width: 8px;
		background-color: #AEB3BD;
	}

	:global(::-webkit-scrollbar-thumb) {
		border-radius: 10px;
		/* -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2); */
		background-color: rgba(113, 106, 133, 0.25);
	}




</style>