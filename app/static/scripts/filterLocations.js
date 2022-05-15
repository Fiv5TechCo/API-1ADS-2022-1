let jobs = ''
let jobsToAdd = ''

async function getJobs() {
  let data = await fetch("https://raw.githubusercontent.com/YagoPSilva/Compilado-API/main/app/models/for_Metricas.json?token=GHSAT0AAAAAABQZH6WERI5GPQUQBWTRYQCAYUA4W6A")
  jobs = await data.json()
  return jobs
}

async function updateJobs() {

    jobsToAdd = await getJobs()

    const jobs = document.querySelector("div.jobs")
    
    jobsToAdd.map((job) => {

      const jobTitle = job["task"]
      const jobWage = job["wage"]
      const jobLocation = job["place"]
      
      jobs.innerHTML += `
      <div class="job">
      <h5>${jobTitle}</h5>
      <p>Salário: ${jobWage}</p>
      <p class="location">Localidade: ${jobLocation}</p>
      </div>
      `
    })

    if (getCookie() == '') {
    } else {
      const location = document.cookie.split(";")[0].split("=")[1].toString()
      return filterLocation(location)
    }
}

function filterLocation(location) {
  const searchBox = document.querySelector("input#searchbox")
  searchBox.value = location
  const input = location
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

function getLocation() {
  const input = document.querySelector("input#searchbox").value
  document.cookie = `name=${input}`
  const location = document.cookie.split(";")[0].split("=")[1].toString()
  return filterLocation(location)
}

function getCookie() {
  const cookie = document.cookie
  return cookie
}


updateJobs()
