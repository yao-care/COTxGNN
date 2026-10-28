---
layout: default
title: Dimenhydrinate
parent: Solo Predicción del Modelo (L5)
nav_order: 223
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Dimenhydrinate: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L4). Indicación original: Dimenhidrinato"
monitor_inn: "dimenhydrinate"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dimenhydrinate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Dimenhidrinato: De Dimenhidrinato (indicación original sin especificar) a Urticaria Alérgica
{: .text-alpha }

## Resumen en Una Frase

Dimenhidrinato es una sal de difenhidramina y 8-cloroteofilina; en Colombia sus registros sanitarios solo mencionan el nombre del principio activo como indicación, sin detallar el uso clínico.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**,
con **0 ensayos clínicos** y **1 publicación** (un estudio farmacocinético en perros) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dimenhidrinato (el registro no detalla una indicación específica) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 0.9974 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Comercializado (registros vigentes: al menos 2) |
| Número de Registros Sanitarios | 2 (ambos cancelados) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el dimenhidrinato es una sal de difenhidramina y 8-cloroteofilina. La difenhidramina es un antihistamínico H1 de primera generación que bloquea la roncha y el eritema mediados por histamina, por lo que mecanísticamente podría ser aplicable a la urticaria alérgica.

La difenhidramina ya se utiliza clínicamente en reacciones alérgicas agudas y urticaria, y el dimenhidrinato actuaría a través del mismo componente. El puntaje de TxGNN (0.9974) es una predicción computacional y no constituye evidencia clínica.

Hay limitaciones prácticas importantes: las guías actuales prefieren antihistamínicos H1 de segunda generación, no sedantes, y la carga sedante y anticolinérgica de los agentes de primera generación, sumada a que los registros están cancelados, reduce su valor práctico.

Como referencia secundaria, el modelo también predice **urticaria por frío** (puntaje 0.9924, nivel L5, sin ensayos ni publicaciones). La plausibilidad mecanística es similar (antagonismo H1), pero la evidencia es solo predictiva y las guías ya cuentan con alternativas (antihistamínicos de segunda generación a dosis altas u omalizumab).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Estudio farmacocinético piloto (en perros sanos) | Veterinary Dermatology | Evaluó la farmacocinética de la difenhidramina tras administración oral e intravenosa, y del dimenhidrinato oral, junto con el efecto sobre la formación de ronchas inducidas por histamina. Demuestra exposición al componente activo, pero no aporta datos de eficacia en urticaria humana. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19950623 (cancelado) | DIMENOL® TABLETAS | Tableta | Dimenhidrinato |
| 20158112 (cancelado) | MARE-OFF® | Tableta | Dimenhidrinato |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia el fármaco con contraindicación en las siguientes condiciones:
  - Cardiovasculares: hipertensión, trastornos hipotensivos, síndrome coronario agudo, enfermedad arterial coronaria, infarto de miocardio, trombosis coronaria.
  - Hepáticas y digestivas: enfermedad hepática, enfermedad de la vesícula biliar, úlcera péptica, estenosis pilórica.
  - Metabólicas y endocrinas: diabetes mellitus, hiperglucemia, cetoacidosis diabética, hipertiroidismo, enfermedad de Graves, tirotoxicosis, hipofosfatemia, gota.
  - Hematológicas: trombocitopenia, trastornos de la coagulación, hemoglobinopatías.
  - Oculares: glaucoma de ángulo cerrado, hipertensión ocular.
  - Urológicas: hiperplasia prostática benigna, obstrucción del cuello vesical.
  - Otras: abuso o dependencia de sustancias.
- **Interacciones Farmacológicas**: se identificaron 67 interacciones; las más relevantes de la muestra disponible son:
  - **Mayores**: cloruro de potasio y citrato de potasio.
  - **Moderadas**: anticolinérgicos y antimuscarínicos (atropina, hiosciamina, escopolamina, glicopirronio, diciclomina, clidinio, trospio, propantelina, metescopolamina, mepenzolato), opioides (morfina, opio, loperamida, eluxadolina), nabilona, metoclopramida y prucaloprida.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a plausibilidad mecanística y a un estudio farmacocinético veterinario sin datos de eficacia en urticaria. Además, existen alternativas preferidas (antihistamínicos de segunda generación), el perfil sedante y anticolinérgico es desfavorable, y los dos registros sanitarios en Colombia están cancelados.

**Para avanzar se necesita:**
- Datos de eficacia clínica del dimenhidrinato (o de la difenhidramina) en urticaria alérgica, idealmente ensayos controlados.
- Información del mecanismo de acción y del prospecto aprobado (advertencias y contraindicaciones), ya que no hay datos disponibles.
- Evaluación del valor frente a los antihistamínicos de segunda generación ya disponibles.
- Análisis de la viabilidad regulatoria, dado que no hay registros vigentes en Colombia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

