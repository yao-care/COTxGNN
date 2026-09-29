---
layout: default
title: Ramucirumab
parent: Solo Predicción del Modelo (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Ramucirumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Ramucirumab: De Indicación Oncológica No Especificada en el Registro a Adenocarcinoma del Ligamento Uterino

## Resumen en Una Frase

Ramucirumab es un anticuerpo que bloquea el receptor VEGFR2 y está comercializado en Colombia como CYRAMZA®. El texto del registro sanitario solo repite el nombre del principio activo y no detalla la indicación original.
El modelo TxGNN predice que podría ser efectivo para **adenocarcinoma del ligamento uterino**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción basada únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto aprobado solo dice "RAMUCIRUMAB") |
| Nueva Indicación Predicha | Adenocarcinoma del ligamento uterino |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información disponible, ramucirumab es un anticuerpo que bloquea VEGFR2, un receptor clave de la angiogénesis (formación de nuevos vasos sanguíneos que alimentan al tumor). Mecanísticamente, bloquear esta vía podría ser aplicable a los adenocarcinomas ginecológicos.

La relación con la indicación original es difícil de evaluar porque el registro no la detalla. Los datos sugieren que el fármaco se usa en adenocarcinomas gastrointestinales, y por eso algunas predicciones tienen una analogía histológica débil, como las variantes de células en anillo de sello e intestinal del adenocarcinoma mucinoso cervical.

Hay que ser prudentes. No se recuperó ningún ensayo ni publicación que vincule ramucirumab con esta entidad. Además, "adenocarcinoma del ligamento uterino" es una entidad extremadamente rara y probablemente un nodo de la ontología, más que una población clínica real. Las otras nueve predicciones principales (adenocarcinoma endocervical, carcinoma adenoide quístico del cuello uterino y otras variantes ginecológicas) tienen puntajes casi idénticos (≈99.94%) y el mismo nivel de evidencia L5. La más plausible clínicamente es el carcinoma endocervical, donde la vía VEGF ya se aprovecha con bevacizumab (un anticuerpo contra VEGF-A).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20111011 | CYRAMZA® (ELI LILLY & COMPANY) | Solución concentrada para infusión | RAMUCIRUMAB |

Nota: el paquete de datos muestra 5 entradas, todas con el mismo número de registro 20111011, y reporta 20 registros en total.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal contra VEGFR2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.95%), pero es solo del modelo (L5). No hay ensayos ni publicaciones, y la entidad predicha es tan rara que probablemente no corresponde a una población clínica real.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de INVIMA para completar la información de seguridad (advertencias y contraindicaciones), que hoy bloquea el tamizaje de seguridad.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Aclarar la indicación original aprobada en Colombia, porque el registro solo muestra el nombre del principio activo.
- Buscar evidencia directa de ramucirumab en cáncer de cuello uterino o ginecológico. Se sugiere priorizar el carcinoma endocervical sobre las entidades ultra raras.
- Verificar si "adenocarcinoma del ligamento uterino" corresponde a una población clínica real o solo a un nodo de la ontología.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

