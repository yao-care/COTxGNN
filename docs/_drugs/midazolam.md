---
layout: default
title: Midazolam
parent: Solo Predicción del Modelo (L5)
nav_order: 283
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Midazolam: De Indicación No Especificada en el Registro a Insomnio

## Resumen en Una Frase

Midazolam es una benzodiacepina de acción corta, comercializada en Colombia como solución inyectable. El registro sanitario no detalla su indicación original: el texto solo repite el nombre del fármaco.
El modelo TxGNN predice que podría ser efectivo para **insomnio**. Esta dirección cuenta con **4 ensayos clínicos publicados de tipo ECA en la literatura (1981-1990)**, aunque de los **32 ensayos registrados** ninguno evalúa midazolam como tratamiento directo del insomnio.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice «Midazolam») |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L2 (basado en ECAs publicados en literatura; ver la nota en la conclusión) |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la farmacología conocida de la clase, midazolam es un modulador alostérico positivo de los receptores GABA-A. Potencia la señalización inhibitoria GABAérgica, lo que produce efecto sedante-hipnótico, acorta la latencia del sueño y aumenta su duración. Este mecanismo es inferido de la clase y no proviene del registro suministrado.

Este mecanismo es el mismo de otras benzodiacepinas hipnóticas, como flurazepam, que se usan en el insomnio. Su vida media muy corta y su inicio rápido encajan con las dificultades para conciliar el sueño. El puntaje alto de TxGNN es coherente con esta farmacología.

Los ECAs históricos apoyan la predicción. Midazolam oral mostró eficacia hipnótica en pacientes con insomnio secundario a enfermedades neuromusculares y musculoesqueléticas. Las principales preocupaciones de seguridad de la clase son los efectos residuales al día siguiente, la tolerancia, la dependencia y el insomnio de rebote.

## Evidencia de Ensayos Clínicos

Se identificaron 32 ensayos, y solo se muestran los más relevantes. Ninguno prueba midazolam como tratamiento del insomnio primario. En la mayoría, el sueño es un desenlace secundario en contextos perioperatorios o de cuidados intensivos, o midazolam es solo el comparador.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Fase 4 | Completado | 111 | Calidad del sueño postoperatorio con sedación de dexmedetomidina vs. midazolam en resección transuretral de próstata. Es el ensayo más pertinente (relevancia B), pero el contexto es perioperatorio y midazolam actúa como comparador |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | N/A | Reclutando | 280 | Midazolam oral preoperatorio frente a placebo sobre el dolor postoperatorio en pacientes con trastorno del sueño o ansiedad sometidos a cirugía colorrectal laparoscópica |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminado | 5 | Sueño medido por polisomnografía de 24 h con dexmedetomidina vs. midazolam en pacientes ventilados en UCI. Terminado con muy pocos participantes |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Fase 1 | Terminado | 6 | Polisomnografía en pacientes ventilados sedados con agonistas α2 vs. agonistas GABA. Terminado con muy pocos participantes |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | N/A | Completado | 23 | Dexmedetomidina vs. midazolam para facilitar la extubación en pacientes de UCI. No mide sueño |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Fase 3 | Desconocido | 120 | Dexmedetomidina vs. midazolam para sedación en niños críticos ventilados. Evalúa sedación, no insomnio |
| [NCT04149626](https://clinicaltrials.gov/study/NCT04149626) | Fase 2 | Desconocido | 60 | Sedación con dexmedetomidina, midazolam o remifentanilo en cirugía ortopédica bajo anestesia regional. Midazolam es comparador |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Fase 3 | Aún no recluta | 195 | Melatonina oral vs. midazolam oral como premedicación en niños sometidos a amigdalectomía. El objetivo es la ansiedad |
| [NCT06480500](https://clinicaltrials.gov/study/NCT06480500) | Fase 2 | Reclutando | 110 | TCC por internet más ketamina intravenosa para suicidalidad en depresión resistente, con midazolam como control activo |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | ECA | Br J Clin Pharmacol | Doble ciego en 30 mujeres con insomnio secundario a enfermedad neuromuscular. Midazolam 15 mg fue un hipnótico eficaz, mejor tolerado que Vesparax y sin causar resaca al día siguiente |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | ECA | J Clin Psychopharmacol | Estudio multicéntrico doble ciego que comparó flurazepam y midazolam durante 14 días en insomnes crónicos. Evalúa sueño, desempeño y niveles plasmáticos |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | ECA | J Clin Psychopharmacol | Resumen ejecutivo del mismo estudio multicéntrico de 14 días con flurazepam y midazolam (sin resumen disponible) |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | ECA | Arzneimittel-Forschung | Búsqueda de dosis (10-30 mg por vía oral) en 75 pacientes hospitalizados con insomnio leve a moderado. Se determinó el rango óptimo de dosis |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Uso clínico de hipnóticos: las benzodiacepinas con distintos perfiles farmacocinéticos son clínicamente eficaces, y se discute la necesidad de contar con varios hipnóticos |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Revisión | Orvosi Hetilap | Revisión sobre insomnio e hipoperfusión cerebral. Es contexto general y no aborda midazolam |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Otro (estudio piloto) | J Clin Med | Lemborexant para insomnio y prevención de delirio tras procedimientos endoscópicos bajo sedación profunda. Señala que las benzodiacepinas podrían aumentar el delirio |
| [22729271](https://pubmed.ncbi.nlm.nih.gov/22729271/) | 2013 | Preclínico | Psychopharmacology | Efectos de zolpidem sobre sedación, ansiedad y memoria en modelo animal. Es evidencia de otro hipnótico |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Preclínico | Pain | Alteración del sueño en un modelo murino de dolor neuropático asociada a cambios en la transmisión GABAérgica en la corteza cingulada |

## Información de Mercado en Colombia

Se registran 20 entradas de licencia. Las 5 primeras corresponden al mismo registro sanitario, por lo que se muestra una sola vez.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20198997 | RELACUM® SOLUCION INYECTABLE (Laboratorios PISA S.A. de C.V.) | Solución inyectable | Midazolam (el registro no detalla la indicación) |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se cuenta con advertencias ni contraindicaciones del registro sanitario, y no se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existen ECAs históricos de midazolam oral en insomnio y el mecanismo es coherente, pero esa evidencia es antigua (1981-1990). Ninguno de los 32 ensayos registrados prueba midazolam como tratamiento del insomnio, y ni la Fase 2/3 completada que exige el nivel L2 ni un ensayo Fase 3 completado en insomnio están presentes, por lo que el nivel L2 debe leerse con cautela. Además, los datos de seguridad locales faltan por completo, y la única presentación registrada en Colombia es inyectable, mientras que los ECAs usaron la vía oral.

**Para avanzar se necesita:**
- Obtener el prospecto de INVIMA con advertencias y contraindicaciones (brecha bloqueante de seguridad)
- Confirmar el mecanismo de acción en DrugBank
- Verificar la indicación aprobada real del registro sanitario 20198997
- Evaluar la compatibilidad de vía de administración, dado que la presentación local es inyectable y la evidencia de insomnio es oral
- Revisar la seguridad frente a alternativas actuales, considerando efectos residuales, tolerancia, dependencia e insomnio de rebote
- Buscar evidencia contemporánea (ECAs recientes) que confirme la eficacia en insomnio

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

