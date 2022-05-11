const vagas = [
  {
    titulo: "Desenvolvedor Front-end",
    descricao: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, sapiente",
    localizacao: "São José dos Campos / SP"
  },
  {
    titulo: "Desenvolvedor Back-end",
    descricao: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, sapiente",
    localizacao: "Jacareí / SP"
  },
  {
    titulo: "Desenvolvedor FullStack",
    descricao: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Placeat, sapiente",
    localizacao: "Caçapava / SP"
  }
]

function updateJobs() {

  const jobs = document.querySelector("div.jobs")
  
  vagas.map((job) => {
    const jobTitle = job.titulo
    const jobDescription = job.descricao
    const jobLocation = job.localizacao
    
    jobs.innerHTML += `
        <div class="job">
          <h5>${jobTitle}</h5>
          <p>Descrição da vaga: ${jobDescription}</p>
          <p class="location">Localidade: ${jobLocation}</p>
        </div>
    `
  })
}

updateJobs()

function filterLocation() {
  const input = document.querySelector("input#searchbox").value
  const filter = input.toLowerCase()
  const divJobs = document.querySelector("div.jobs")
  const divJobsItems = divJobs.getElementsByClassName('job')
  for(var i=0; i<divJobsItems.length; i++){
    const links = divJobsItems[i].getElementsByClassName("location")[0]
    if(links.innerHTML.toLowerCase().indexOf(filter)>-1) {
      divJobsItems[i].style.display=""
    } else {
      divJobsItems[i].style.display="none"
    }
  }
}