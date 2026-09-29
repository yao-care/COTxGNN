---
layout: default
title: Capecitabine
parent: Solo Predicción del Modelo (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabina: De Cáncer de Mama y Colorrectal Metastásico a Adenocarcinoma Gástrico con Poliposis Gástrica Proximal

## Resumen en Una Frase

Capecitabina es un profármaco oral de fluoropirimidina, utilizado originalmente para el cáncer de mama y colorrectal metastásico.
El modelo TxGNN predice que podría ser efectivo para **adenocarcinoma gástrico y poliposis proximal del estómago (GAPPS)**, un síndrome hereditario muy raro.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación específica, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama y colorrectal metastásico (según los datos de farmacología; en INVIMA el texto de indicación solo dice «CAPECITABINA») |
| Nueva Indicación Predicha | Adenocarcinoma gástrico y poliposis proximal del estómago |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, capecitabina es un profármaco que la timidina fosforilasa convierte en 5-fluorouracilo (5-FU). El 5-FU inhibe la timidilato sintasa (TYMS), enzima necesaria para sintetizar ADN, y así frena la proliferación de células tumorales. Esto coincide con el dato farmacológico registrado, donde TYMS aparece como su diana humana.

Capecitabina tiene eficacia comprobada en tumores del tubo digestivo, y el adenocarcinoma gástrico es un tumor epitelial sensible a las fluoropirimidinas. Por eso un efecto citotóxico en células de adenocarcinoma gástrico es mecanísticamente plausible.

Sin embargo, la GAPPS es un síndrome hereditario raro. No se recuperó ningún ensayo ni publicación específica para esta entidad, así que la razonabilidad se apoya solo en el mecanismo general y no en evidencia propia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20155908 | KAPIXA® 500 MG TABLETAS RECUBIERTAS (XINETIX PHARMA S.A.S.) | Tableta recubierta | CAPECITABINA (el registro no detalla la indicación) |

Nota: los 5 registros listados en los datos corresponden al mismo número de registro sanitario (20155908), por lo que se muestran una sola vez. El total reportado es de 20 registros.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, clase fluoropirimidina) |
| Riesgo de Mielosupresión | Medio (según conocimiento general de la clase; no hay datos de toxicidad en el Evidence Pack) |
| Clasificación de Emetogenicidad | Baja (según la categoría del fármaco) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal; consultar el prospecto para parámetros adicionales |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y solo devolvió su diana farmacológica, la timidilato sintasa (TYMS). Esto describe el mecanismo y no una interacción entre medicamentos.

Consultar el prospecto para las advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para GAPPS solo existe la predicción del modelo (L5). No se encontraron ensayos ni literatura, y la enfermedad es hereditaria y muy rara.

Otras indicaciones gástricas predichas tienen más respaldo, por ejemplo el adenocarcinoma tubular gástrico y el carcinoma del cuerpo gástrico (ambas L1, con varios ECA de Fase 3 que usan capecitabina, sobre todo como CAPOX, dentro de combinaciones). Esos usos ya son estándar de tratamiento, por lo que corresponden a confirmación de indicación y no a reposicionamiento propiamente dicho.

**Para avanzar se necesita:**
- Búsqueda dirigida de casos, series o guías sobre GAPPS y quimioterapia con fluoropirimidinas
- Datos del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto INVIMA
- Definir si conviene evaluar como candidato principal una de las indicaciones gástricas con mayor evidencia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

