let jobs;
let jobsJson;
let jobsToAdd;
let cities = []
let states = []
let locations = []

async function getJobs() {
  await fetch(`https://raw.githubusercontent.com/Fiv5TechCo/API-1ADS-2022-1/main/app/models/for_Metricas.json`)
  .then( response => response.json())
  .then( json => jobsJson = json)
  .catch( err => console.log(err))
  return jobsJson
}

async function updateJobs() {
  
  jobsToAdd = await getJobs()

  const jobs = document.querySelector("div.jobs")
  const select = document.querySelector('select#searchbox')

  jobsToAdd.map((job) => {

    const jobTitle = job["task"]
    const jobWage = job["wage"]
    const jobLocation = job["place"]

    updateLocations(jobLocation)

    jobs.innerHTML += `
      <div class="job">
      <h5>${jobTitle}</h5>
      <p>Salário: ${jobWage}</p>
      <p class="location">Localidade: ${jobLocation}</p>
      </div>
      `
  })

  let index = 0
  cities.forEach(city => {
    let concat = (`${cities[index]} / ${states[index]}`)
    if (locations.indexOf(concat) == -1) {
      locations.push(concat)
    }
    index++
  })

  locations = locations.sort()

  locations.forEach(location => {
    select.innerHTML += `<option value="${location}" name="coordinates">${location}</option>`
  })

  if (getCookie() == '') {
  } else {
    const location = document.cookie.split(";")[0].split("=")[1].toString()
    return filterLocation(location)
  }
}

function filterLocation(location) {
  const searchBox = document.querySelector("select#searchbox")
  searchBox.value = location
  const input = location
  const filter = input.toLowerCase()
  const divJobs = document.querySelector("div.jobs")
  const divJobsItems = divJobs.getElementsByClassName('job')
  for (var i = 0; i < divJobsItems.length; i++) {
    const links = divJobsItems[i].getElementsByClassName("location")[0]
    if (links.innerHTML.toLowerCase().indexOf(filter) > -1) {
      divJobsItems[i].style.display = ""
    } else {
      divJobsItems[i].style.display = "none"
    }
  }
}

function getLocation() {
  const input = document.querySelector("select#searchbox").value
  document.cookie = `name=${input}`
  const location = document.cookie.split(";")[0].split("=")[1].toString()
  return filterLocation(location)
}

function getCookie() {
  const cookie = document.cookie
  return cookie
}

function updateLocations(jobLocation) {
  let cityToAdd = jobLocation.split(',')
  let stateToAdd;

  if (cityToAdd.length == 1) {
    stateToAdd = jobLocation.split(' / ')[1]
    cityToAdd = jobLocation.split(' / ')[0]
  } else {
    cityToAdd = cityToAdd[1].split(' / ')
    stateToAdd = cityToAdd[1]
    cityToAdd = cityToAdd[0]
  }

  if (cityToAdd[0] == ' ') {
    cityToAdd = cityToAdd.slice(2)
  }

  cities.push(cityToAdd)
  states.push(stateToAdd)

}

document.addEventListener('DOMContentLoaded', updateJobs())