const graph1 = document.querySelector('div#graph-1')
const graph2 = document.querySelector('div#graph-2')
const graph3 = document.querySelector('div#graph-3')
const graph4 = document.querySelector('div#graph-4')

function render() {
  let selectValue = document.querySelector("#myselect").value
  switch(selectValue) {
    case "vagas_estado":
      console.log(selectValue)
      graph1.style.display = `block`
      graph2.style.display = `none`
      graph3.style.display = `none`
      graph4.style.display = `none`
      break
    case "vagas_area":
      console.log(selectValue)
      graph1.style.display = `none`
      graph2.style.display = `block`
      graph3.style.display = `none`
      graph4.style.display = `none`
      break
    case "cursos_area":
      console.log(selectValue)
      graph1.style.display = `none`
      graph2.style.display = `none`
      graph3.style.display = `block`
      graph4.style.display = `none`
      break
    case "mapa_calor":
      console.log(selectValue)
      graph1.style.display = `none`
      graph2.style.display = `none`
      graph3.style.display = `none`
      graph4.style.display = `block`
      break
  }
}


document.addEventListener('DOMContentLoaded', render())