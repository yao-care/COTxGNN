---
layout: default
title: Adenosine
parent: Solo Predicción del Modelo (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Adenosina: De Indicación No Especificada a Bloqueo de Rama del Haz (término obsoleto)

## Resumen en Una Frase

Adenosina es un fármaco inyectable que se ha registrado en Colombia bajo el nombre del principio activo; el texto de indicación del registro no detalla su uso específico, aunque la farmacología conocida la asocia con el tratamiento de taquicardias.
El modelo TxGNN predice que podría ser efectivo para **bloqueo de rama del haz (término obsoleto en la ontología)**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
Como alternativa más plausible aparece la **taquicardia ventricular polimórfica catecolaminérgica (TVPC)**, con 0 ensayos clínicos y un único reporte de caso directamente relacionado.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | ADENOSINA (el registro no detalla la indicación; la farmacología conocida la vincula con el tratamiento de taquicardias) |
| Nueva Indicación Predicha | Bloqueo de rama del haz (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 4 (todos cancelados) |
| Decisión Recomendada | Hold |

**Candidata secundaria:** taquicardia ventricular polimórfica catecolaminérgica (puntaje TxGNN 99.42%, nivel de evidencia L4, clasificación "Pregunta de investigación").

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, la adenosina actúa sobre los receptores de adenosina A1, A2A, A2B y A3, además de interactuar con TRPM4 y con las fosfatidilinositol 4-quinasas tipo 2 alfa y beta. Su uso clínico reconocido es el tratamiento de taquicardias, y actúa como bloqueador del nodo auriculoventricular.

**Bloqueo de rama del haz:** la única base de esta predicción es el puntaje del modelo. No se recuperaron ensayos ni literatura, y el término está marcado como obsoleto en la ontología, por lo que probablemente es un nodo heredado o duplicado y no una entidad clínica distinta. La adenosina se usa de forma diagnóstica en trastornos de conducción, pero los datos no respaldan una justificación para tratar este trastorno.

**Taquicardia ventricular polimórfica catecolaminérgica (TVPC):** esta enfermedad se debe a una fuga de calcio del retículo sarcoplásmico y a postdespolarizaciones tardías (actividad desencadenada) bajo estimulación adrenérgica. La adenosina, a través de los receptores A1, antagoniza la actividad desencadenada mediada por AMPc y catecolaminas, lo que ofrece una base mecanística plausible para terminar la taquicardia asociada a TVPC. La evidencia clínica directa se limita a un reporte de caso en el que el trifosfato de adenosina terminó una taquicardia ventricular bidireccional. Esto respalda, como máximo, un uso agudo o diagnóstico, no un tratamiento crónico ni preventivo. El manejo estándar (betabloqueadores, flecainida, denervación simpática, DAI) está bien establecido, por lo que la adenosina sería, a lo sumo, un complemento o herramienta diagnóstica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados, ni para bloqueo de rama del haz ni para TVPC.

---

## Evidencia de Literatura

Para la indicación principal (bloqueo de rama del haz) actualmente no hay literatura relacionada disponible. Para la candidata secundaria (TVPC) se identificó la siguiente literatura relevante:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Reporte de caso | Heart Rhythm | El trifosfato de adenosina terminó una taquicardia ventricular bidireccional en un paciente con TVPC |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Declaración de consenso / Revisión | Europace | Consenso internacional sobre el papel diagnóstico de las pruebas de provocación farmacológica en electrofisiología cardíaca |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Observación clínica | Heart Rhythm | Repolarización anormal tras estimulación en TVPC asociada a mutación del receptor de rianodina cardíaco |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Revisión | J Assoc Physicians India | Reconocimiento y manejo de la taquicardia ventricular en corazones estructuralmente normales |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Revisión | Paediatric Anaesthesia | Arritmias pediátricas que debe conocer el anestesiólogo |
| [15324613](https://pubmed.ncbi.nlm.nih.gov/15324613/) | 2004 | Revisión | Curr Treat Options Cardiovasc Med | Alternativas de tratamiento del síncope |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Preclínico (modelo in vitro) | J Physiol | Microtejidos cardio-neurales humanos muestran que la TVPC también afecta a la neurona simpática |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclínico (terapia génica) | Cardiovasc Res | La terapia génica con PDE2A y PDE4B mejora la insuficiencia cardíaca y las arritmias en ratones |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Preclínico (mecanístico) | Commun Biol | La deficiencia de TECRL altera la función mitocondrial en cardiomiocitos |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclínico (animal) | Sci Transl Med | La fuga de calcio del retículo sarcoplásmico contribuye a la arritmia pero no a la progresión de la insuficiencia cardíaca |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20148959 | ADENOTROY | Solución inyectable | ADENOSINA (cancelado) |
| 20139028 | ADENOSINA SOLUCIÓN INYECTABLE 6MG/2ML | Solución inyectable | ADENOSINA (cancelado) |
| 20272824 | TAKIKARD® 6 MG/2 ML SOLUCIÓN INYECTABLE | Solución inyectable | ADENOSINA (cancelado) |
| 20058380 | ADENOSINA 6MG / 2 ML SOLUCIÓN INYECTABLE | Solución inyectable | ADENOSINA (cancelado) |

---

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento (no provienen del prospecto):** el grafo de conocimiento del modelo asocia la adenosina con las siguientes enfermedades como posibles contraindicaciones:
  - **Respiratorias:** enfermedad pulmonar obstructiva crónica (EPOC), asma (intrínseco y alérgico), enfisema pulmonar, insuficiencia respiratoria.
  - **Valvulares:** estenosis aórtica (incluida la supravalvular), enfermedad de la válvula aórtica, estenosis mitral, insuficiencia de la válvula pulmonar.
  - **Conducción y ritmo:** bloqueo auriculoventricular, síndrome del seno enfermo (incluida la forma familiar).
  - **Otras cardiovasculares:** síndrome coronario agudo, enfermedad arterial coronaria, pericarditis, trastornos hipotensivos.
  - **Neurológicas:** enfermedad del sistema nervioso autónomo, síndrome de Horner.
- **Interacciones farmacológicas / dianas:** se registraron 7 interacciones farmacológicas con dianas, todas de tipo farmacológico y sin nivel de severidad asignado: receptores A1, A2A, A2B y A3 de adenosina, TRPM4, PI4K2A y PI4K2B.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación principal predicha (bloqueo de rama del haz) se sostiene solo en el puntaje del modelo, sin ensayos ni literatura, y corresponde a un término obsoleto de la ontología. Además, los cuatro registros sanitarios en Colombia están cancelados. La TVPC es una línea de investigación más plausible (L4), pero la evidencia se limita a un reporte de caso, con un posible uso agudo o diagnóstico y no terapéutico crónico.

**Para avanzar se necesita:**
- Aclarar si el término "bloqueo de rama del haz" corresponde a una entidad clínica vigente o a un nodo duplicado en la ontología.
- Obtener el prospecto de INVIMA para completar la información de advertencias y contraindicaciones oficiales (brecha de datos bloqueante para el cribado de seguridad).
- Obtener los datos del mecanismo de acción desde DrugBank.
- Definir si la hipótesis de TVPC se orienta a uso diagnóstico/agudo, y explorarla con revisión sistemática o estudios de series de casos.
- Evaluar la situación regulatoria: confirmar por qué los registros fueron cancelados y si existe alternativa de acceso al producto en Colombia.
- Revisar con cuidado las contraindicaciones del grafo de conocimiento (en especial EPOC, asma, bloqueo AV y síndrome del seno enfermo) frente a cualquier uso propuesto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

