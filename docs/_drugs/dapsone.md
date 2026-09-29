---
layout: default
title: Dapsone
parent: Evidencia Alta (L1-L2)
nav_order: 148
evidence_level: L1
indication_count: 1
---

# Dapsone
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Dapsona: De Indicación No Especificada en el Registro a Neumocistosis

## Resumen en Una Frase

La dapsona es una sulfona que se usa clásicamente contra la lepra, la dermatitis herpetiforme y la profilaxis de la neumonía por *Pneumocystis*. El registro colombiano solo consigna el nombre "DAPSONA" como texto de indicación.
El modelo TxGNN predice que podría ser efectiva para **neumocistosis**, con **14 ensayos clínicos** registrados y **ninguna publicación** suministrada en el paquete de evidencia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto figura solo como "DAPSONA") |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 3 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según el conocimiento farmacológico general, la dapsona inhibe la dihidropteroato sintasa y bloquea la síntesis de folato en *Pneumocystis jirovecii*. Los datos farmacológicos incluidos apuntan en la misma dirección: inhibe la actividad de la dihidrofolato reductasa en *Pneumocystis carinii* (CI50 de 1.5 µM *in vitro*) y actúa sobre la enzima dihidropteroato sintasa de *Plasmodium falciparum*. Es la misma vía que atacan las sulfonamidas como el sulfametoxazol.

La fuente farmacológica describe el uso clínico conocido de la dapsona: lepra (dentro de un esquema multifármaco), dermatitis herpetiforme y profilaxis de la neumonía por *Pneumocystis* en personas inmunodeprimidas, en especial pacientes con sida. Por eso esta predicción es en gran medida confirmatoria: la neumocistosis ya es un uso clínico establecido, sobre todo como alternativa cuando no se tolera el trimetoprim-sulfametoxazol.

El puntaje TxGNN (0.997) coincide con la evidencia clínica, pero no es independiente de ella. La profilaxis es el uso mejor respaldado. La evidencia de tratamiento se limita a esquemas combinados, como dapsona con trimetoprim.

## Evidencia de Ensayos Clínicos

Se muestran 10 de los 14 ensayos registrados, los más relevantes.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Fase 3 | Completado | 700 | Dapsona diaria vs. atovacuona diaria para profilaxis de PCP en pacientes con VIH intolerantes a trimetoprim o sulfonamidas |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Fase 3 | Completado | 290 | Dapsona/trimetoprim y clindamicina/primaquina vs. trimetoprim/sulfametoxazol en PCP leve a moderada en sida |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Fase 3 | Completado | 400 | Pentamidina en aerosol mensual vs. dapsona tres veces por semana para profilaxis de PCP en pacientes intolerantes a trimetoprim o sulfonamidas |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Fase 3 | Completado | 600 | Tres agentes anti-*Pneumocystis* más zidovudina en infección avanzada por VIH; el título está truncado y la presencia de dapsona como brazo debe verificarse |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | No aplica | Completado | No reportada | Dapsona 100 mg vs. 50 mg como profilaxis primaria de PCP; informa sobre la dosis y la tolerabilidad a largo plazo |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Fase 1 | Completado | 96 | Dapsona diaria vs. semanal en niños con VIH: toxicidad, farmacocinética y fallas de profilaxis |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Fase 1 | Completado | 20 | Trimetrexato con leucovorina más dapsona vs. TMP/SMX en PCP moderadamente grave; seguridad y farmacocinética |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | No aplica | Completado | No reportada | Dapsona vs. trimetoprim-sulfametoxazol en el primer episodio de PCP en sida; efectividad, efectos adversos y aptitud para manejo ambulatorio |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | No aplica | Completado | 30 | Clindamicina con TMP/SMX para PCP tras trasplante de órgano sólido; la dapsona se menciona solo como alternativa de segunda línea (contexto) |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Fase 4 | Desconocido | 3130 | Tamizaje genético HLA-B*1301 para prevenir el síndrome de hipersensibilidad a dapsona; su relación con PCP no se puede confirmar |

## Informacion de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20148515 | DAPSULON® 50 MG | Tableta cubierta con película | DAPSONA |
| 20145596 | DAPSULON® 100 MG | Tableta | DAPSONA |

El titular de ambos es LIMINAL THERAPEUTICS S.A.S. El paquete de datos reporta 3 registros en total, pero el registro 20145596 aparece dos veces con datos idénticos. Además, el texto de indicación solo repite el nombre del fármaco, por lo que no se puede confirmar si la neumocistosis figura como indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias y contraindicaciones del registro no están disponibles.

Como precauciones (basadas en conocimiento farmacológico general, no en el prospecto de INVIMA):
- Tamizar por deficiencia de G6PD antes de usar, por el riesgo de hemólisis.
- Vigilar la aparición de metahemoglobinemia.
- El ensayo NCT02550080 apunta a un riesgo de síndrome de hipersensibilidad a dapsona asociado a HLA-B*1301.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Al menos tres ensayos de Fase 3 completados comparan directamente esquemas con dapsona en la prevención o el tratamiento de la neumonía por *Pneumocystis* (NCT00000802, NCT00000640, NCT00001028), lo que sostiene el nivel L1. La evidencia de profilaxis es sólida, pero la de tratamiento se limita a combinaciones, y la ficha de seguridad local está incompleta.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA (advertencias y contraindicaciones) y verificar si la neumocistosis consta como indicación aprobada o sería uso fuera de indicación.
- Completar el mecanismo de acción desde DrugBank.
- Realizar una búsqueda de literatura, ya que no se suministró ninguna publicación.
- Confirmar que la dapsona es un brazo del ensayo NCT00000991.
- Definir un protocolo de tamizaje de G6PD y de monitoreo de metahemoglobinemia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

