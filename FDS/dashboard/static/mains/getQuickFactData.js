import { RatioGraph, RunChart, getRandomColors } from "./components/Plottings.js";

const endpoint = "https://fds.atri.org.tw/graphql/";
const headers = {
  "content-type": "application/json",
};

const optionsCreate = (props) => {
  const select = document.querySelector(`#${props.id}`);
  select.options.length = 1; // Clear options except the first one

  props.data.forEach((d) => {
    const option = document.createElement("option");
    option.value = d;
    option.innerHTML = d;
    select.appendChild(option);
  });
};

const setQuery = (props) => {
    const query = {
      query: `query ${props.queryName} ($year: Int!, $sector: String) {
        ${props.queryName} (year:$year, sector: $sector) {
          ${props.queryName === "stageshareByYearAndSector" ? "FarmGate TransGate ProcessGate TradeGate Year{Year}" :
              props.queryName === "marketingByYearAndSector" ? "FarmShare MarketingShare Year{Year}" :
              props.queryName === "industryByYearAndSector" ? "Agribusiness FarmProduction FoodProcess Packaging Transportation WholesaleTrade RetailTrade Trade FoodService Energy FinanceInsurance Advertising Accounting Year{Year}" :
              props.queryName === "primaryByYearAndSector" ? "Compensation OperatingSurplus ConsumptionOfFixedCapital NetTaxes Adjustment Imports Year{Year}" :
              ""}
        }
      }`,
      variables: {
        year: parseInt(props.year),
        sector: props.sector,
      }
    };
    return query;
  }

const getStageShare = async (props) => {
  const query = setQuery({queryName: "stageshareByYearAndSector", year: props.year, sector: props.sector})
  const options = {
    url: endpoint,
    method: "post",
    headers: headers,
    data: query,
  };

  try {
    const response = await axios.request(options);
    const res = response.data.data.stageshareByYearAndSector.map((d) => ({
      FarmGate: d.FarmGate,
      TransGate: d.TransGate,
      ProcessGate: d.ProcessGate,
      TradeGate: d.TradeGate,
    }));
    RunChart(res);
  } catch (error) {
    console.error(error);
  }
};

const getSharingData = async (props, chartName, chartAreaId) => {
  const query = setQuery({
    queryName: chartName, year: props.year, sector: props.sector
  });
  const options = {
    url: endpoint,
    method: "post",
    headers: headers,
    data: query,
  };

  if (chartName == 'industryByYearAndSector') {
    var query_for_marketing = setQuery({
      queryName: "marketingByYearAndSector", year: props.year, sector: props.sector
    });
    console.log(query_for_marketing);
    var options_for_marketing = {
      url: endpoint,
      method: "post",
      headers: headers,
      data: query_for_marketing,
    };
  }

  try {
    const theYear = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container .theYear');
    const response = await axios.request(options);
    const res = response.data.data;
    const data = res[chartName][0];
    const numColors = Object.keys(data).length;
    const colors = getRandomColors(numColors);
    const year = data.Year.Year;
    if (data.MarketingShare) {
      const FarmShareValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #FarmShareValue');
      const MarketingShareValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #MarketingShareValue')
      FarmShareValue.innerHTML = data.FarmShare.toFixed(1);
      MarketingShareValue.innerHTML = data.MarketingShare.toFixed(1);
    } else if (data.FarmProduction) {
      const response_marketing = await axios.request(options_for_marketing);
      const res_marketing = response_marketing.data.data;
      const data_marketing = res_marketing["marketingByYearAndSector"][0];
      const FarmShareValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #FarmShare');
      const ImplyingValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #ImplyingValue');
      const FarmProductionValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #FarmProductionValue');
      const RetailTradeValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #RetailTradeValue');
      const FoodServiceValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #FoodServiceValue');
      const EnergyValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #EnergyValue');
      const AdvertisingValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #AdvertisingValue');
      const IndustryGroupValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #IndustryGroupValue');
      FarmProductionValue.innerHTML = data.FarmProduction.toFixed(1);
      RetailTradeValue.innerHTML = data.RetailTrade.toFixed(1);
      FoodServiceValue.innerHTML = data.FoodService.toFixed(1);
      EnergyValue.innerHTML = data.Energy.toFixed(1);
      AdvertisingValue.innerHTML = data.Advertising.toFixed(1);
      IndustryGroupValue.innerHTML = (data.RetailTrade + data.FoodService).toFixed(1);
      FarmShareValue.innerHTML = data_marketing.FarmShare.toFixed(1);
      ImplyingValue.innerHTML = (data_marketing.FarmShare - data.FarmProduction).toFixed(1);
    } else if (data.Compensation) {
      const CompensationValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #CompensationValue');
      const OperatingSurplusValue = document.querySelector('.' + chartAreaId.substring(0, chartAreaId.length - 4) + 'Container #OperatingSurplusValue')
      CompensationValue.innerHTML = data.CompensationValue.toFixed(1);
      OperatingSurplusValue.innerHTML = data.OperatingSurplusValue.toFixed(1);
    }
    theYear.innerHTML = year;
    const props = {
      chartName,
      chartAreaId,
      data,
      colors,
    };
    RatioGraph(props);
  } catch (error) {
    console.error(error);
  }
}

const getSectors = async (data) => {
  const SectorQuery = {
    query: `query stageshareByYearAndSector($year: Int!, $sector: String) { 
      stageshareByYearAndSector (year:$year, sector: $sector) {
        Sector{
          Name
        }
      }
    }`,
    variables: {
      year: data,
      sector: "",
    },
  };

  const options = {
    url: endpoint,
    method: "post",
    headers: headers,
    data: SectorQuery,
  };

  try {
    const response = await axios.request(options);
    const res = response.data.data;
    let data = res.stageshareByYearAndSector.map((d) => d.Sector.Name);
    data = data.filter((element, index, self) => self.indexOf(element) === index);
    optionsCreate({ id: "sectors", parentID: "StageShareArea", data });
    const plottingSelector = document.querySelector("#plottings");
    const sectorSelector = document.querySelector("#sectors");
    sectorSelector.addEventListener("change", (event) => {
      if (sectorSelector.value !== "0" && plottingSelector.value === "Stage Share") {
        getStageShare({
          year: document.querySelector("#years").value,
          sector: document.querySelector("#sectors").value,
        });
      }else if(sectorSelector.value !== "0" && plottingSelector.value === "Marketing bill") {
        getSharingData({
          year: document.querySelector("#years").value,
          sector: document.querySelector("#sectors").value,
        }, "marketingByYearAndSector", "MarketingShareArea");
      }else if(sectorSelector.value !== "0" && plottingSelector.value === "Industry group") {
        getSharingData({
          year: document.querySelector("#years").value,
          sector: document.querySelector("#sectors").value,
        }, "industryByYearAndSector", "IndustryShareArea");
      }else if(sectorSelector.value !== "0" && plottingSelector.value === "Primary factor") {
        getSharingData({
          year: document.querySelector("#years").value,
          sector: document.querySelector("#sectors").value,
        }, "primaryByYearAndSector", "PrimaryShareArea");
      }
    });
  } catch (error) {
    console.error(error);
  }
};

const getData = async () => {
  const YearQuery = {
    query: `query { allYears { Year } }`,
    variables: {},
  };

  const options = {
    url: endpoint,
    method: "post",
    headers: headers,
    data: YearQuery,
  };

  try {
    const response = await axios.request(options);
    const res = response.data.data;

    const plottingSelector = document.querySelector("#plottings");
    const StageShareContainer = document.querySelector(".StageShareContainer");
    const MarketingShareContainer = document.querySelector(".MarketingShareContainer");
    const IndustryShareContainer = document.querySelector(".IndustryShareContainer");
    const PrimaryShareContainer = document.querySelector(".PrimaryShareContainer");
    plottingSelector.addEventListener("change", (event) => {
      StageShareContainer.style.display = plottingSelector.value === "Stage Share" ? "flex" : "none";
      MarketingShareContainer.style.display = plottingSelector.value === "Marketing bill" ? "flex" : "none";
      IndustryShareContainer.style.display = plottingSelector.value === "Industry group" ? "flex" : "none";
      PrimaryShareContainer.style.display = plottingSelector.value === "Primary factor" ? "flex" : "none";
    });

    const data = res.allYears.map((d) => d.Year);
    await Promise.all([
      optionsCreate({ id: "years", parentID: "StageShareArea", data }),
      getStageShare({ year: Math.max(...data), sector: "整體農食" }),
      getSharingData({ year: Math.max(...data), sector: "整體農食" }, "marketingByYearAndSector", "MarketingShareArea"),
      getSharingData({ year: Math.max(...data), sector: "整體農食" }, "industryByYearAndSector", "IndustryShareArea"),
      getSharingData({ year: Math.max(...data), sector: "整體農食" },"primaryByYearAndSector", "PrimaryShareArea"),
    ]);

    const yearSelector = document.querySelector("#years");
    yearSelector.addEventListener("change", (event) => {
      if (yearSelector.value !== "0") {
        document.querySelector("#sectors").style.visibility = "visible";
        getSectors(parseInt(yearSelector.value));
      } else {
        document.querySelector("#sectors").style.visibility = "hidden";
      }
    });
  } catch (error) {
    console.error(error);
  }
};

getData();


