---
layout: default
title: Darunavir
parent: Evidencia Moderada (L3-L4)
nav_order: 149
evidence_level: L4
indication_count: 4
---

# Darunavir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Darunavir: De Combinación Ritonavir + Darunavir (antirretroviral) a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Darunavir es un inhibidor de la proteasa del VIH-1, autorizado en Colombia en combinación con ritonavir dentro de regímenes antirretrovirales.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (FIV)**,
pero solo hay **1 ensayo clínico** (en VIH-1 humano, evidencia indirecta) y **ninguna publicación** que respalde directamente esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Combinaciones (ritonavir y darunavir) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según el conocimiento general, darunavir es un inhibidor de la proteasa del VIH-1 y se usa junto con ritonavir, que actúa como potenciador farmacocinético. Su eficacia en la infección por VIH-1 en humanos está comprobada.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus emparentado con el VIH, lo que da un vínculo plausible pero no demostrado. La proteasa del FIV es estructuralmente distinta a la del VIH-1, por lo que la actividad y la potencia en gatos son inciertas. El puntaje TxGNN (~0.9997) probablemente refleja la red compartida de fármacos antirretrovirales y lentivirus, y no datos específicos en felinos.

Además, esta es una indicación veterinaria. No corresponde a una nueva indicación en humanos dentro del registro sanitario colombiano.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Completado | 145 | Estudio aleatorizado y abierto que compara darunavir/ritonavir + lamivudina frente a darunavir/ritonavir + tenofovir/emtricitabina (o tenofovir/lamivudina) en adultos con VIH-1 sin tratamiento previo. Es evidencia en humanos, no en felinos ni en FIV, por lo que solo respalda de forma indirecta. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Hay 8 registros sanitarios en total. La tabla muestra los productos únicos, porque varios registros aparecen repetidos con el mismo número.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20109284 | VIRONTAR N COMPRIMIDOS RECUBIERTOS (Laboratorios Richmond S.A.C.I.F.) | Tableta recubierta | Combinaciones (ritonavir y darunavir) |
| 20109025 | VIRONTAR (Laboratorios Richmond S.A.C.I.F.) | Comprimido | Darunavir + ritonavir |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay evidencia directa en felinos ni en FIV, y el único ensayo disponible es en VIH-1 humano. La actividad de darunavir sobre la proteasa del FIV es incierta y el puntaje alto del modelo probablemente refleja la red de antirretrovirales. Las otras predicciones del modelo tampoco tienen respaldo suficiente:
- **Infección por virus de inmunodeficiencia de simio (SIV):** solo estudios en macacos, sin ensayos en humanos.
- **Trastorno del neurodesarrollo raro:** sin evidencia ni vínculo mecanístico claro.
- **Hiperlipidemia combinada familiar:** término obsoleto, y los inhibidores de proteasa se asocian a dislipidemia.

**Para avanzar se necesita:**
- Estudios in vitro de actividad de darunavir frente a la proteasa del FIV
- Estudios veterinarios de eficacia y seguridad en gatos
- Datos de mecanismo de acción confirmados desde DrugBank
- Advertencias y contraindicaciones del prospecto de INVIMA para el análisis de seguridad
- Confirmar si esta indicación veterinaria está dentro del alcance del proyecto

*Este informe es solo para fines de investigación y no constituye consejo médico ni veterinario. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

