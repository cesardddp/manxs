const Editor = {
    compilerOptions: {
        delimiters: ['@{', '}']
    },
    data() {
        return {
            titulo_data: "",
            banner_data: "",
            feitos_data: "",
            texto_historico_data: "",
            musicas_data: "",
            texto_final_data: "",
            texto_principal_data: "",
            card_missao_data: "",
            card_objetivo_data: "",
            instagrams_data: "",
        }
    },
    methods: {
        teste: _.debounce(function (event) {
            console.log(
                // this.$data
            )
            let text = event.target.textContent
            let id = event.target.id
            debugger

            axios
                .patch(
                    '/editor/edit/' + id,
                    { data: text }
                    //substitui pela url de busca
                )
                .then(response => {
                    debugger

                })
                .catch(error => {
                    alert('Erro! Não foi possível adquirir resultados da API: ' + error)
                })

        }, 550)

    }


}
const app = Vue.createApp(Editor)
app.mount("#app_editor")
