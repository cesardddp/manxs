<template>
    <header class="d-flex flex-wrap justify-content-center mb-3">
        <a href="/" class="navbar-brand mb-1"> <img loading="lazy" src="../assets/logo_manxs.png" alt width="60"
                class="d-inline-block"> <b class="fs-3 link-light align-middle">MANXS</b> </a>

        <ul class="nav col-12 mb-2 justify-content-center menu1">
            <li class="   "><a href="/                        " class="nav-link px-2 link-light">HOME</a></li>
            <li class="dropdown active_menu"> <a class="nav-link px-2 link-light dropdown-toggle"
                    id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">BIOGRAFIA</a>
                <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                    <li><a class="dropdown-item" href="/biografia/">HISTÓRIA</a></li>
                    <li><a class="dropdown-item disabled" href="#">Ashilleyy</a></li>
                    <li><a class="dropdown-item disabled" href="#">Vikky</a></li>
                    <li><a class="dropdown-item disabled" href="#">LuisAfF</a></li>
                </ul>
            </li>
            <li class><a href="/servicos/" class="nav-link px-2 link-light">SERVIÇOS</a></li>
            <li class=" "><a href="/galeria/ " class="nav-link px-2 link-light">GALERIA</a></li>
            <li class="  "><a href="/videos/ " class="nav-link px-2 link-light">VIDEOS</a></li>
            <li class="   "><a href="/shows/" class="nav-link px-2 link-light">SHOWS</a></li>
            <li class=" "><a href="/musicas/" class="nav-link px-2 link-light">MUSICAS</a></li>
            <li class=" "><a href="/contato/" class="nav-link px-2 link-light">CONTATO</a></li>
        </ul>
    </header>
    <div class="hero-image" :style="bg">teste</div>

</template>
<script setup lang='ts'>
    // importe ref 
    import { ref } from "vue";

    const bg = ref({
        
    })
</script>
<style>
header {
    background-image: linear-gradient(to top right, pink, rgba(0, 0, 0, 0.699)), url('../assets/imgs/holofortes.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: unset;
}
</style>