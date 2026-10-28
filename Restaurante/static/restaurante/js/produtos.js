
const form = document.getElementById("form")
const nome = document.getElementById("nome")
const categoria = document.getElementById("cat")
const subcategoria = document.getElementById("subcat")
const subcat_comidas =["entradas","fastfood","sobremesas","pratos principais"]
const subcat_bebidas =["agua","refrigerante","cerveja","sumos naturais","whisky","vinho","coktail","sumo"]

categoria.addEventListener("change", (e)=>{
    const valor = e.target.value
    console.log(valor)
    if (valor == "comida"){
        subcategoria.innerHTML= `<option value="" selected disabled>Selecione uma opção</option>`
        for(const i of subcat_comidas){
            const option = document.createElement("option")
            option.value=i
            option.textContent=i.charAt(0).toUpperCase()+i.slice(1)
            subcategoria.appendChild(option)
        }
    }
    else if (valor == "bebida"){
        subcategoria.innerHTML=`<option value="" selected disabled>Selecione uma opção</option>`
        for (const i of subcat_bebidas){
            const option = document.createElement("option")
            option.value=i
            option.textContent=i.charAt(0).toUpperCase() + i.slice(1)
            subcategoria.appendChild(option)

        }
    }
})

