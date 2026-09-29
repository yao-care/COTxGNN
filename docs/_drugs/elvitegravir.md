---
layout: default
title: Elvitegravir
parent: Evidencia Moderada (L3-L4)
nav_order: 174
evidence_level: L4
indication_count: 3
---

# Elvitegravir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Elvitegravir: De Infección por VIH-1 a Infección por el Virus de la Inmunodeficiencia Simia (SIV)

## Resumen en Una Frase

Elvitegravir es un inhibidor de la integrasa del VIH, usado como componente de la combinación antirretroviral Genvoya (elvitegravir, cobicistat, emtricitabina y tenofovir alafenamida).
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la inmunodeficiencia simia (SIV)**,
pero hoy solo hay **0 ensayos clínicos** y **7 publicaciones** preclínicas (in vitro y en animales) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | El texto del registro solo lista los componentes de la combinación (elvitegravir, cobicistat, emtricitabina, tenofovir alafenamida) y no describe la indicación. Se asume infección por VIH-1 por la clase del fármaco; debe confirmarse en el prospecto. |
| Nueva Indicación Predicha | Infección por el virus de la inmunodeficiencia simia (SIV) |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Elvitegravir es un inhibidor de la transferencia de cadena de la integrasa (INSTI) del VIH-1. Bloquea la integración del ADN viral en el genoma de la célula huésped. Actualmente no se dispone de datos detallados de mecanismo de acción en la ficha del fármaco, pero esta descripción corresponde a su clase farmacológica.

La integrasa del SIV es estructuralmente muy parecida a la del VIH-1. La literatura recuperada es coherente con actividad de clase contra el SIV: hay estudios in vitro de susceptibilidad y de mutaciones de resistencia en SIVmac239, y modelos animales con SIV/SHIV. Esto explica por qué el modelo asigna un puntaje alto.

Hay una limitación importante. El SIV es una infección de primates no humanos que se usa como modelo experimental del VIH. La evidencia es por tanto indirecta y preclínica, y no respalda una nueva indicación en humanos. Las otras dos predicciones del modelo (síndrome de inmunodeficiencia adquirida felina y un trastorno del neurodesarrollo raro) tienen solo nivel L5, sin ensayos ni literatura. La segunda no tiene ningún vínculo mecanístico plausible y probablemente es un artefacto del grafo de conocimiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Preclínico in vivo | J Infect Dis | Inserciones vaginales con tenofovir alafenamida (20 mg) y elvitegravir (16 mg) protegieron a macacos frente a exposiciones vaginales repetidas a SHIV: 93% de protección al administrarse 4 horas antes y 100% 4 horas después de la exposición. El estudio evalúa profilaxis posexposición extendida. |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclínico in vivo | Front Immunol | Modelo de ratón humanizado de doble propósito para probar estrategias antivirales contra SIV y VIH, como alternativa de animal pequeño a los modelos en primates. |
| [17977962](https://pubmed.ncbi.nlm.nih.gov/17977962/) | 2008 | In vitro | J Virol | Elvitegravir bloquea la integración del ADNc del VIH-1 al inhibir la transferencia de cadena. Inhibe la replicación de distintos subtipos y de virus multirresistentes, y se describe su perfil de resistencia. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In vitro | J Virol | Caracteriza los perfiles de resistencia de los INSTI en SIVmac239 mediante selección en cultivo celular con células de macaco rhesus. Compara si aparecen las mismas mutaciones que en el VIH. |
| [25583721](https://pubmed.ncbi.nlm.nih.gov/25583721/) | 2015 | In vitro | Antimicrob Agents Chemother | Usa un virus recombinante SIV/VIH de tropismo simio como modelo para estudiar la resistencia a inhibidores de la integrasa. |
| [24920794](https://pubmed.ncbi.nlm.nih.gov/24920794/) | 2014 | In vitro | J Virol | Mutaciones de resistencia del VIH-1 (seleccionadas con raltegravir, elvitegravir y dolutegravir) introducidas en SIVmac239 para evaluar su efecto en la susceptibilidad a los INSTI. |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro | Antimicrob Agents Chemother | Actividad de bictegravir y cabotegravir frente a SIVmac239 y VIH-1 resistentes a INSTI. Menciona a raltegravir y elvitegravir como INSTI aprobados con menor barrera genética. |

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20111795 | GENVOYA ® TABLETAS RECUBIERTAS | Tableta recubierta (oral) | Composición: elvitegravir, cobicistat, emtricitabina, tenofovir alafenamida (el registro no detalla la indicación) |

El paquete de datos informa 20 registros en total, pero las 5 entradas recibidas corresponden al mismo registro sanitario (20111795) y se muestran una sola vez.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es solo preclínica (L4): estudios in vitro y en modelos animales de SIV/SHIV, sin ningún ensayo clínico. El SIV es una infección de primates no humanos, por lo que no constituye una indicación humana nueva.

**Para avanzar se necesita:**
- Confirmar la indicación original (VIH-1) y el mecanismo de acción en el prospecto oficial del INVIMA.
- Obtener del prospecto las advertencias, contraindicaciones e interacciones, que hoy no están disponibles.
- Definir si existe un caso de uso real (por ejemplo, investigación veterinaria o modelos de profilaxis en primates), ya que no hay una necesidad clínica humana asociada.
- Descartar las predicciones de nivel L5 (síndrome de inmunodeficiencia felina y trastorno del neurodesarrollo) salvo que aparezca evidencia nueva.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

