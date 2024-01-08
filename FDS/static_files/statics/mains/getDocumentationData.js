import { RatioGraph, getRandomColors } from "./components/Plottings.js";

const endpoint = "http://fds.atri.org.tw/graphql/";
const headers = {
  "content-type": "application/json",
};


const fetchData = async (query, chartName, chartAreaId) => {
  const options = {
    url: endpoint,
    method: "post",
    headers: headers,
    data: query,
  };

  try {
    const response = await axios.request(options);
    const res = response.data.data;
    const data = res[chartName][0];
    const numColors = Object.keys(data).length;
    const colors = getRandomColors(numColors);
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
};

const fetchAllData = async (data) => {
  try {
    const YearQuery = {
      query: `{ allYears { Year } }`,
      variables: {},
    };

    const options = {
      url: endpoint,
      method: "post",
      headers: headers,
      data: YearQuery,
    };

    const response = await axios.request(options);
    const res = response.data.data;
    const latestYear = Math.max(...res.allYears.map((d) => d.Year));

    const PrimaryQuery = {
      query: `query primaryByYearAndSector($year: Int!, $sector: String!) { 
                primaryByYearAndSector (year:$year, sector: $sector) {
                  Compensation
                  OperatingSurplus
                  ConsumptionOfFixedCapital
                  NetTaxes
                  Adjustment
                  Imports
                }
              }`,
      variables: {
        year: latestYear,
        sector: "整體農食",
      },
    };

    const IndustryQuery = {
      query: `query industryByYearAndSector($year: Int!, $sector: String!) { 
                industryByYearAndSector (year:$year, sector: $sector) {
                  Agribusiness
                  FarmProduction
                  FoodProcess
                  Packaging
                  Transportation
                  WholesaleTrade
                  RetailTrade
                  FoodService
                  Energy
                  FinanceInsurance
                  Advertising
                  Sector{
                    Name
                  }
                }
              }`,
      variables: {
        year: latestYear,
        sector: "整體農食",
      },
    };

    const MarketingQuery = {
      query: `query marketingByYearAndSector($year: Int!, $sector: String!) { 
                marketingByYearAndSector (year:$year, sector: $sector) {
                  FarmShare
                  MarketingShare
                  Sector{
                    Name
                  }
                }
              }`,
      variables: {
        year: latestYear,
        sector: "整體農食",
      },
    };

    await Promise.all([
      fetchData(PrimaryQuery, "primaryByYearAndSector", "Primary"),
      fetchData(IndustryQuery, "industryByYearAndSector", "Industry"),
      fetchData(MarketingQuery, "marketingByYearAndSector", "Marketing"),
    ]);
  } catch (error) {
    console.error(error);
  }
};

fetchAllData();
