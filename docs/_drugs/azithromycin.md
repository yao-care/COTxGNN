---
layout: default
title: Azithromycin
parent: Solo Predicción del Modelo (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azitromicina: De Antibacteriano Macrólido (Indicación No Detallada en el Registro) a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

La azitromicina es un antibiótico macrólido de administración oral, comercializado en Colombia.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de hiperviscosidad policlonal**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No detallada en los registros (el texto del registro solo dice «Azitromicina») |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la azitromicina es un antibiótico macrólido, su eficacia antibacteriana está ampliamente comprobada, y su perfil farmacológico incluye interacción con el receptor de motilina (MLNR) y con el receptor del gusto amargo TAS2R4. Sin embargo, no existe un vínculo mecanístico documentado con el síndrome de hiperviscosidad policlonal.

El síndrome de hiperviscosidad policlonal es una condición en la que la sangre se vuelve más espesa de lo normal por exceso de proteínas (inmunoglobulinas). No se recuperó ningún ensayo ni publicación que relacione la azitromicina con este cuadro. Por eso, la puntuación alta del modelo (99.81%) debe leerse como una señal para explorar, no como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en Colombia

Los registros recibidos tenían la misma licencia repetida cuatro veces; aquí se muestran una sola vez. Las formas farmacéuticas reportadas son tableta y tableta recubierta, ambas de vía oral.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 19911014 | PENFLUZ 500 MG TABLETAS | Tableta | Azitromicina (el registro no detalla indicaciones) |
| 20068317 | AKRIBACT® | Tableta | Azitromicina (el registro no detalla indicaciones) |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no se reportaron interacciones con otros fármacos. Los dos registros recibidos corresponden a dianas farmacológicas de la azitromicina (receptor de motilina y TAS2R4), no a interacciones medicamentosas.

Consultar el prospecto para información de seguridad sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ningún ensayo clínico ni publicación de respaldo (nivel L5), y no hay un mecanismo plausible documentado. La azitromicina está ampliamente disponible en Colombia, pero eso no sustituye la evidencia para esta nueva indicación.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank para evaluar un posible vínculo con la hiperviscosidad.
- Descargar y revisar el prospecto de INVIMA para completar advertencias y contraindicaciones.
- Hacer una búsqueda de literatura más amplia y dirigida al síndrome de hiperviscosidad policlonal.
- Considerar otras predicciones del mismo análisis con algo más de señal:
  - **Gammapatía monoclonal**: hay un estudio preclínico in vitro (PMID 23546223) en el que macrólidos, incluida la azitromicina, bloquean la autofagia y sensibilizan células de mieloma a bortezomib. Está catalogada como pregunta de investigación (L4).
  - **Trastorno hematológico congénito (enfermedad de células falciformes)**: hay dos ensayos de azitromicina directamente relacionados (NCT02630394 y NCT02960503), pero ambos fueron retirados con 0 participantes, por lo que no aportan datos clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

