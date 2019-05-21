# sdg-graph-query-api
API for querying complex paths between different types of SDG-related content


# Example reuqest & response

```
curl -X POST \
  http://localhost:5000/api \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 20420d8c-52df-4708-9a83-2b812f190900' \
  -H 'cache-control: no-cache' \
  -d '[
    {
        "url": "http://metadata.un.org/thesaurus#1005064"
    },
	{
        "url": "http://metadata.un.org/thesaurus#1005064"
    },
    {
        "url": "http://eurovoc.europa.eu/2281"
    },
    {
        "url": "http://eurovoc.europa.eu/2062"
    },
    {
        "url": "http://metadata.un.org/thesaurus#1000544"
    },
    {
        "url": "http://eurovoc.europa.eu/6781"
    },
    {
        "url": "http://metadata.un.org/thesaurus#1006166"
    }
]'
```

In the reponse, the value of the `count` property reflects the relative importance of the given entity / concept in the results.

```
{
    "http://data.un.org/kos/sdg/01.01": {
        "count": 24,
        "type": "Target",
        "label": "01.01 By 2030, eradicate extreme poverty for all people everywhere, currently measured as people living on less than $1.25 a day",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 4
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 4
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 4
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 4
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 4
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 4
            }
        }
    },
    "http://data.un.org/kos/sdg/01": {
        "count": 184,
        "type": "Goal",
        "label": "01 End poverty in all its forms everywhere",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 69
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 23
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 23
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 23
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 23
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 23
            }
        }
    },
    "http://data.un.org/kos/sdg/01.02": {
        "count": 14,
        "type": "Target",
        "label": "01.02 By 2030, reduce at least by half the proportion of men, women and children of all ages living in poverty in all its dimensions according to national definitions",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 4
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 2
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 2
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 2
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 2
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 2
            }
        }
    },
    "http://data.un.org/kos/sdg/01.03": {
        "count": 102,
        "type": "Target",
        "label": "01.03 Implement nationally appropriate social protection systems and measures for all, including floors, and by 2030 achieve substantial coverage of the poor and the vulnerable",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 17
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 17
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 17
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 17
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 17
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 17
            }
        }
    },
    "http://data.un.org/kos/sdg/01.04": {
        "count": 3,
        "type": "Target",
        "label": "01.04 By 2030, ensure that all men and women, in particular the poor and the vulnerable, have equal rights to economic resources, as well as access to basic services, ownership and control over land and other forms of property, inheritance, natural resources, appropriate new technology and financial services, including microfinance",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 3
            }
        }
    },
    "http://data.un.org/kos/sdg/01.05": {
        "count": 33,
        "type": "Target",
        "label": "01.05 By 2030, build the resilience of the poor and those in vulnerable situations and reduce their exposure and vulnerability to climate-related extreme events and other economic, social and environmental shocks and disasters",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 33
            }
        }
    },
    "http://data.un.org/kos/sdg/01.0a": {
        "count": 5,
        "type": "Target",
        "label": "01.0a Ensure significant mobilization of resources from a variety of sources, including through enhanced development cooperation, in order to provide adequate and predictable means for developing countries, in particular least developed countries, to implement programmes and policies to end poverty in all its dimensions",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 5
            }
        }
    },
    "http://data.un.org/kos/sdg/01.0b": {
        "count": 2,
        "type": "Target",
        "label": "01.0b Create sound policy frameworks at the national, regional and international levels, based on pro-poor and gender-sensitive development strategies, to support accelerated investment in poverty eradication actions",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 2
            }
        }
    },
    "http://data.un.org/kos/sdg/C010101": {
        "count": 18,
        "type": "Indicator",
        "label": "01.01.01 Proportion of population below the international poverty line, by sex, age, employment status and geographical location (urban/rural)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 3
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 3
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 3
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 3
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 3
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 3
            }
        }
    },
    "http://data.un.org/kos/sdg/C010201": {
        "count": 12,
        "type": "Indicator",
        "label": "01.02.01 Proportion of population living below the national poverty line, by sex and age",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 2
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 2
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 2
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 2
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 2
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 2
            }
        }
    },
    "http://data.un.org/kos/sdg/C010202": {
        "count": 1,
        "type": "Indicator",
        "label": "01.02.02 Proportion of men, women and children of all ages living in poverty in all its dimensions according to national definitions",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/C010301": {
        "count": 96,
        "type": "Indicator",
        "label": "01.03.01 Proportion of population covered by social protection floors/systems, by sex, distinguishing children, unemployed persons, older persons, persons with disabilities, pregnant women, newborns, work-injury victims and the poor and the vulnerable",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 16
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 16
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 16
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 16
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 16
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 16
            }
        }
    },
    "http://data.un.org/kos/sdg/C010401": {
        "count": 1,
        "type": "Indicator",
        "label": "01.04.01 Proportion of population living in households with access to basic services",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/C010402": {
        "count": 1,
        "type": "Indicator",
        "label": "01.04.02 Proportion of total adult population with secure tenure rights to land, (a) with legally recognized documentation, and (b) who perceive their rights to land as secure, by sex and type of tenure",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/C010502": {
        "count": 9,
        "type": "Indicator",
        "label": "01.05.02 Direct economic loss attributed to disasters in relation to global gross domestic product (GDP)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 9
            }
        }
    },
    "http://data.un.org/kos/sdg/C010a01": {
        "count": 1,
        "type": "Indicator",
        "label": "01.0a.01 Proportion of domestically generated resources allocated by the government directly to poverty reduction programmes",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/C010a02": {
        "count": 2,
        "type": "Indicator",
        "label": "01.0a.02 Proportion of total government spending on essential services (education, health and social protection)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 2
            }
        }
    },
    "http://data.un.org/kos/sdg/C010a03": {
        "count": 1,
        "type": "Indicator",
        "label": "01.0a.03 Sum of total grants and non-debt-creating inflows directly allocated to poverty reduction programmes as a proportion of GDP",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/C010b01": {
        "count": 1,
        "type": "Indicator",
        "label": "01.0b.01 Proportion of government recurrent and capital spending to sectors that disproportionately benefit women, the poor and vulnerable groups",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/C200303": {
        "count": 16,
        "type": "Indicator",
        "label": "01.05.01/11.05.01/13.01.01 Number of deaths, missing persons and directly affected persons attributed to disasters per 100,000 population",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 16
            }
        }
    },
    "http://data.un.org/kos/sdg/11.05": {
        "count": 24,
        "type": "Target",
        "label": "11.05 By 2030, significantly reduce the number of deaths and the number of people affected and substantially decrease the direct economic losses relative to global gross domestic product caused by disasters, including water-related disasters, with a focus on protecting the poor and people in vulnerable situations",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 24
            }
        }
    },
    "http://data.un.org/kos/sdg/13.01": {
        "count": 23,
        "type": "Target",
        "label": "13.01 Strengthen resilience and adaptive capacity to climate-related hazards and natural disasters in all countries",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 23
            }
        }
    },
    "http://data.un.org/kos/sdg/11": {
        "count": 33,
        "type": "Goal",
        "label": "11 Make cities and human settlements inclusive, safe, resilient and sustainable",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 32
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/13": {
        "count": 23,
        "type": "Goal",
        "label": "13 Take urgent action to combat climate change and its impacts",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 23
            }
        }
    },
    "http://data.un.org/kos/sdg/C200304": {
        "count": 3,
        "type": "Indicator",
        "label": "01.05.03/11.0b.01/13.01.02 Number of countries that adopt and implement national disaster risk reduction strategies in line with the Sendai Framework for Disaster Risk Reduction 2015-2030",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 3
            }
        }
    },
    "http://data.un.org/kos/sdg/11.0b": {
        "count": 7,
        "type": "Target",
        "label": "11.0b By 2020, substantially increase the number of cities and human settlements adopting and implementing integrated policies and plans towards inclusion, resource efficiency, mitigation and adaptation to climate change, resilience to disasters, and develop and implement, in line with the Sendai Framework for Disaster Risk Reduction 2015-2030, holistic disaster risk management at all levels",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 7
            }
        }
    },
    "http://data.un.org/kos/sdg/C200305": {
        "count": 4,
        "type": "Indicator",
        "label": "01.05.04/11.0b.02/13.01.03 Proportion of local governments that adopt and implement local disaster risk reduction strategies in line with national disaster risk reduction strategies",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 4
            }
        }
    },
    "http://data.un.org/kos/sdg/EN_LND_SLUM": {
        "count": 2,
        "type": "Series",
        "label": "Proportion of urban population living in slums (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/C110101": {
        "count": 2,
        "type": "Indicator",
        "label": "11.01.01 Proportion of urban population living in slums, informal settlements or inadequate housing",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/11.01": {
        "count": 2,
        "type": "Target",
        "label": "11.01 By 2030, ensure access for all to adequate, safe and affordable housing and basic services and upgrade slums",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SG_DSR_LEGREG": {
        "count": 1,
        "type": "Series",
        "label": "Countries with legislative and/or regulatory provisions been made for managing disaster risk (1 = YES; 0 = NO)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_BENFTS": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of population covered by at least one social protection benefit (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_CHLD": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of children/households receiving child/family cash benefit (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_DISAB": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of population with severe disabilities receiving disability cash benefit (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_LMKT": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of population covered by labour market programs (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_LMKTPQ": {
        "count": 6,
        "type": "Series",
        "label": "Poorest quintile covered by labour market programs (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_MATNL": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of mothers with newborns receiving maternity cash benefit (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_PENSN": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of population above statutory pensionable age receiving a pension, by sex (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_POOR": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of poor population receiving social assistance cash benefit (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_SOCAST": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of population covered by social assistance programs (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_SOCASTPQ": {
        "count": 6,
        "type": "Series",
        "label": "Poorest quintile covered by social assistance programs (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_SOCINS": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of population covered by social insurance programs (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_SOCINSPQ": {
        "count": 6,
        "type": "Series",
        "label": "Poorest quintile covered by social insurance programs (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_UEMP": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of unemployed persons receiving unemployment cash benefit, by sex (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_VULN": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of vulnerable population receiving social assistance cash benefit (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_COV_WKINJRY": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of employed population covered in the event of work injury (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_POV_DAY1": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of population below international poverty line (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_POV_EMP1": {
        "count": 6,
        "type": "Series",
        "label": "Employed population below international poverty line, by sex and age (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SI_POV_NAHC": {
        "count": 6,
        "type": "Series",
        "label": "Proportion of population living below the national poverty line (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2281": {
                "count": 1
            },
            "http://eurovoc.europa.eu/2062": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            },
            "http://metadata.un.org/thesaurus#1006166": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_AFFCT": {
        "count": 1,
        "type": "Series",
        "label": "Number of people affected by disaster (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_GDPLS": {
        "count": 1,
        "type": "Series",
        "label": "Direct economic loss attributed to disasters (millions of current United States dollars)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/C110502": {
        "count": 8,
        "type": "Indicator",
        "label": "11.05.02 Direct economic loss in relation to global GDP, damage to critical infrastructure and number of disruptions to basic services, attributed to disasters",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 8
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_MISS": {
        "count": 1,
        "type": "Series",
        "label": "Number of missing persons due to disaster (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_MORT": {
        "count": 1,
        "type": "Series",
        "label": "Number of deaths due to disaster (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_DADN": {
        "count": 1,
        "type": "Series",
        "label": "Number damaged dwellings attributed to disasters (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_DAFF": {
        "count": 1,
        "type": "Series",
        "label": "Number of directly affected persons attributed to disasters per 100,000 population (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_DDHN": {
        "count": 1,
        "type": "Series",
        "label": "Number damaged dwellings attributed to disasters, by hazard type (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_DYDN": {
        "count": 1,
        "type": "Series",
        "label": "Number destroyed dwellings attributed to disasters (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_DYHN": {
        "count": 1,
        "type": "Series",
        "label": "Number destroyed dwellings attributed to disasters, by hazard type (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_IJILN": {
        "count": 1,
        "type": "Series",
        "label": "Number of injured or ill people attributed to disasters (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_MMHN": {
        "count": 1,
        "type": "Series",
        "label": "Number of deaths and missing persons attributed to disasters, by hazard type (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_MTMN": {
        "count": 1,
        "type": "Series",
        "label": "Number of deaths and missing persons attributed to disasters (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_MTMP": {
        "count": 1,
        "type": "Series",
        "label": "Number of deaths and missing persons attributed to disasters per 100,000 population (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_PDAN": {
        "count": 1,
        "type": "Series",
        "label": "Number of people whose damaged dwellings were attributed to disasters (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_PDLN": {
        "count": 1,
        "type": "Series",
        "label": "Number of people whose livelihoods were disrupted or destroyed, attributed to disasters (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_PDYN": {
        "count": 1,
        "type": "Series",
        "label": "Number of people whose destroyed dwellings were attributed to disasters (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SG_DSR_LGRGSR": {
        "count": 1,
        "type": "Series",
        "label": "Score of adoption and implementation of national DRR strategies in line with the Sendai Framework",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SG_DSR_SILN": {
        "count": 1,
        "type": "Series",
        "label": "Number of local governments that adopt and implement local DRR strategies in line with national strategies (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SG_DSR_SILS": {
        "count": 1,
        "type": "Series",
        "label": "Proportion of local governments that adopt and implement local disaster risk reduction strategies in line with national disaster risk reduction strategies (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SG_GOV_LOGV": {
        "count": 1,
        "type": "Series",
        "label": "Number of local governments (number)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_AGLH": {
        "count": 1,
        "type": "Series",
        "label": "Direct agriculture loss attributed to disasters, by hazard type (millions of current United States dollars)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_AGLN": {
        "count": 1,
        "type": "Series",
        "label": "Direct agriculture loss attributed to disasters (millions of current United States dollars)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_CHLN": {
        "count": 1,
        "type": "Series",
        "label": "Direct economic loss to cultural heritage damaged or destroyed attributed to disasters (millions of current United States dollars)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_CILN": {
        "count": 1,
        "type": "Series",
        "label": "Direct economic loss resulting from damaged or destroyed critical infrastructure attributed to disasters (millions of current United States dollars)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_HOLH": {
        "count": 1,
        "type": "Series",
        "label": "Direct economic loss in the housing sector attributed to disasters, by hazard type (millions of current United States dollars)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_HOLN": {
        "count": 1,
        "type": "Series",
        "label": "Direct economic loss in the housing sector attributed to disasters (millions of current United States dollars)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/VC_DSR_LSGP": {
        "count": 1,
        "type": "Series",
        "label": "Direct economic loss attributed to disasters relative to GDP (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SD_XPD_ESED": {
        "count": 1,
        "type": "Series",
        "label": "Proportion of total government spending on essential services, education (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1005064": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/03.08": {
        "count": 12,
        "type": "Target",
        "label": "03.08 Achieve universal health coverage, including financial risk protection, access to quality essential health-care services and access to safe, effective, quality and affordable essential medicines and vaccines for all",
        "concept": {
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 6
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 6
            }
        }
    },
    "http://data.un.org/kos/sdg/03": {
        "count": 12,
        "type": "Goal",
        "label": "03 Ensure healthy lives and promote well-being for all at all ages",
        "concept": {
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 6
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 6
            }
        }
    },
    "http://data.un.org/kos/sdg/C030801": {
        "count": 4,
        "type": "Indicator",
        "label": "03.08.01 Coverage of essential health services (defined as the average coverage of essential services based on tracer interventions that include reproductive, maternal, newborn and child health, infectious diseases, non-communicable diseases and service capacity and access, among the general and the most disadvantaged population)",
        "concept": {
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 2
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 2
            }
        }
    },
    "http://data.un.org/kos/sdg/C030802": {
        "count": 6,
        "type": "Indicator",
        "label": "03.08.02 Proportion of population with large household expenditures on health as a share of total household expenditure or income",
        "concept": {
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 3
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 3
            }
        }
    },
    "http://data.un.org/kos/sdg/SH_ACS_UNHC": {
        "count": 2,
        "type": "Series",
        "label": "Universal health coverage (UHC) service coverage index",
        "concept": {
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SH_XPD_EARN10": {
        "count": 2,
        "type": "Series",
        "label": "Proportion of population with large household expenditures on health (greater than 10%) as a share of total household expenditure or income (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            }
        }
    },
    "http://data.un.org/kos/sdg/SH_XPD_EARN25": {
        "count": 2,
        "type": "Series",
        "label": "Proportion of population with large household expenditures on health (greater than 25%) as a share of total household expenditure or income (%)",
        "concept": {
            "http://metadata.un.org/thesaurus#1000544": {
                "count": 1
            },
            "http://eurovoc.europa.eu/6781": {
                "count": 1
            }
        }
    }
}
```