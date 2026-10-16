---
layout: default
title: Clopidogrel
parent: Evidencia Alta (L1-L2)
nav_order: 174
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-14
description: "Clopidogrel: nueva indicación predicha, Trastorno de migraña (migraine disorder) (nivel de evidencia L2). Indicación original: CLOPIDOGREL"
---

# Clopidogrel
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **8** 
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

# Clopidogrel: De Clopidogrel (indicación registrada sin detalle) a Trastorno de Migraña

## Resumen en Una Frase

Clopidogrel es un antiagregante plaquetario (inhibidor del receptor P2Y12) con registros sanitarios en Colombia, hoy cancelados. El modelo TxGNN predice que podría ser eficaz para el **trastorno de migraña** (nueva indicación con mayor respaldo entre las predichas), con **6 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección, sobre todo en migraña asociada a foramen oval permeable (FOP) o posterior al cierre de comunicación interauricular.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CLOPIDOGREL (el registro sanitario no detalla la indicación aprobada) |
| Nueva Indicación Predicha | Trastorno de migraña (migraine disorder) |
| Puntaje de Prediccion TxGNN | 99.44% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Colombia | ✗ Solo registros cancelados |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Proceed with Guardrails |

> Nota: la indicación de mayor puntaje en el modelo es "migraña con aura de tronco encefálico" (99.44%, nivel L3, sin ensayos clínicos, solo evidencia general de migraña con aura). Se presenta como indicación principal el trastorno de migraña, que tiene la evidencia más sólida entre las ocho candidatas.

---

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, clopidogrel inhibe el receptor plaquetario P2Y12, reduce la agregación plaquetaria y se utiliza en la prevención de eventos trombóticos.

La hipótesis de reposicionamiento es que la activación plaquetaria y la embolia paradójica (microémbolos que pasan por un FOP) contribuyen a la migraña con aura. Las plaquetas activadas también liberan serotonina y otros mediadores vasoactivos. Bloquear P2Y12 podría disminuir estos fenómenos. Estudios preclínicos en ratones también implican al receptor P2Y12 en modelos de migraña y en la activación microglial del núcleo caudal del trigémino.

La evidencia es más fuerte en dos escenarios: migraña asociada a FOP y migraña de nueva aparición tras el cierre de comunicación interauricular. En la migraña en general los resultados son mixtos y muchos datos provienen de estudios piloto o retrospectivos.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Fase 4 | Completado | 220 | CANOA: clopidogrel añadido a aspirina para prevenir migraña de nueva aparición tras cierre de comunicación interauricular |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Fase 2 | Completado | 1000 | COMPETE: antiagregante vs. anticoagulante vs. tratamiento estándar de migraña en pacientes con FOP |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Fase 4 | Desconocido | 50 | Eficacia profiláctica de clopidogrel en migraña con cortocircuito derecha-izquierda |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Fase 3 | Activo, sin reclutar | 440 | SPRING: cierre de FOP vs. medicación para aliviar la migraña (no evalúa clopidogrel como intervención) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Completado | 664 | Cierre de FOP vs. anticoagulantes vs. antiagregantes para prevenir recurrencia de ictus (la migraña no es el desenlace principal) |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminado | 7 | Estudio de dispositivo (oclusor septal) para migraña; no es un ensayo de fármaco |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42526943](https://pubmed.ncbi.nlm.nih.gov/42526943/) | 2026 | ECA | BMJ | Ensayo multicéntrico, aleatorizado, abierto, con control activo, sobre tratamiento antitrombótico para prevenir migraña en pacientes con FOP |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | ECA | JAMA | CANOA: clopidogrel más aspirina vs. aspirina sola frente a migraña tras cierre de comunicación interauricular |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | ECA | JAMA Cardiology | Resultados a un año de CANOA tras suspender clopidogrel a los 3 meses |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Revisión sistemática | Headache | Papel de los antitrombóticos en la prevención de la migraña |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Revisión sistemática | Indian J Thorac Cardiovasc Surg | Cefalea de nueva aparición tras cierre de comunicación interauricular |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | ECA piloto | Cephalalgia | Clopidogrel como profilaxis de migraña |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohorte | J Investig Med | Clopidogrel como profilaxis complementaria en migraña refractaria con FOP |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Revisión retrospectiva | Cephalalgia | Clopidogrel como terapia primaria en migrañosos con cortocircuito derecha-izquierda |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Revisión retrospectiva | Neurology | Tienopiridinas en migrañosos con FOP |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Estudio piloto abierto | Neurology | Ticagrelor (otro inhibidor de P2Y12) en migraña refractaria con FOP |

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20198152 (cancelado) | Clopidogrel 75 mg tabletas recubiertas (Laboratorios Richmond) | Tableta recubierta | CLOPIDOGREL |
| 19942021 (cancelado) | Clopidogrel 75 mg tableta recubierta (Laboratorios La Santé) | Tableta recubierta | CLOPIDOGREL |

---

## Consideraciones de Seguridad

- **Contraindicaciones (según relaciones del grafo de conocimiento, no del prospecto):** insuficiencia hepática aguda, hepatitis, trastornos de la coagulación, lesiones traumáticas, púrpura trombocitopénica, úlcera péptica activa y hemorragia intracraneal.
- **Interacciones farmacológicas:** se registraron 100 interacciones. Entre las principales:
  - **Mayores:** rabeprazol, omeprazol, esomeprazol, pioglitazona, loperamida y repaglinida.
  - **Moderadas:** ácido acetilsalicílico, bupropión, morfina, cimetidina, claritromicina, lansoprazol y pantoprazol.
  - **Menores:** dexlansoprazol y glimepirida.
- **Otros puntos de atención en la literatura:** riesgo de sangrado (incluida hemorragia intracerebral al combinarse con AINE) y variabilidad por CYP2C19.

Para advertencias de uso y precauciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay ensayos aleatorizados completados (CANOA y COMPETE) y revisiones sistemáticas que respaldan el uso de clopidogrel en migraña asociada a FOP o posterior al cierre de comunicación interauricular. Fuera de ese fenotipo, la evidencia es mixta y proviene de estudios piloto, por lo que se recomienda avanzar solo con restricciones.

**Para avanzar se necesita:**
- Restringir la población al fenotipo con FOP / migraña con aura.
- Revisar en detalle los resultados del ensayo COMPETE (publicado en BMJ 2026).
- Obtener el prospecto vigente (advertencias y contraindicaciones oficiales) y los datos del mecanismo de acción.
- Plan de monitoreo del riesgo de sangrado, de la variabilidad de CYP2C19 y de las interacciones (especialmente con inhibidores de la bomba de protones y AINE).
- Resolver el estado regulatorio local: ambos registros sanitarios están cancelados, por lo que sería necesario confirmar la disponibilidad comercial en Colombia.

**Otras indicaciones predichas (todas en Hold):** osteoartritis (L4; el único indicio sugiere que clopidogrel no protege), tendinitis, miositis fibrosa, miositis granulomatosa idiopática, artritis reumatoide y susceptibilidad a osteoartritis (L5; solo predicción del modelo). En artritis reumatoide la literatura incluso reporta artritis inflamatoria asociada a clopidogrel como posible señal de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

