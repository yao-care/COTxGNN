---
layout: default
title: Enzalutamide
parent: Solo Predicción del Modelo (L5)
nav_order: 180
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Enzalutamida: De Cáncer de Próstata Avanzado a Susceptibilidad al Cáncer de Próstata/Cerebro

## Resumen en Una Frase

Enzalutamida es un antagonista del receptor de andrógenos, aprobado originalmente para el cáncer de próstata avanzado (metastásico y resistente a la castración).
El modelo TxGNN predice que podría ser efectiva para **susceptibilidad al cáncer de próstata/cerebro**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Los registros sanitarios solo dicen «ENZALUTAMIDA», sin texto de indicación. Según la información farmacológica: cáncer de próstata avanzado (resistente a la castración y sensible a la castración) |
| Nueva Indicación Predicha | Susceptibilidad al cáncer de próstata/cerebro |
| Puntaje de Predicción TxGNN | 99,71 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Enzalutamida bloquea el receptor de andrógenos (AR) en varios pasos: impide la unión del ligando, la translocación al núcleo y la unión al ADN. Por eso se usa en cánceres de próstata dependientes de andrógenos. Los datos de mecanismo de acción de DrugBank no están disponibles, pero la descripción farmacológica del paquete de evidencia confirma este mecanismo.

La predicción tiene una debilidad de fondo. «Susceptibilidad al cáncer de próstata/cerebro» es un fenotipo de predisposición genética, no una enfermedad que se pueda tratar. Por eso no hay un vínculo terapéutico definido. El puntaje alto (99,71 %) proviene solo de asociaciones en el grafo de conocimiento y no se apoya en estudios reales. La relación con la indicación original, que es cáncer de próstata, es de proximidad temática y no de mecanismo comprobado.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20224710 | XTANDI® 40MG TABLETAS (Astellas Pharma US Inc.) | Tableta recubierta | ENZALUTAMIDA (sin texto de indicación) |
| 20198992 | ENZALUTAMIDA 40MG CÁPSULAS BLANDAS (Tecnoquímicas S.A.) | Cápsula blanda | ENZALUTAMIDA (sin texto de indicación) |

Nota: el paquete de evidencia informa 20 registros en total, pero las entradas detalladas solo corresponden a estos 2 números de registro únicos, repetidos varias veces.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (hormonal, antagonista del receptor de andrógenos); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene puntaje alto en el modelo, pero no cuenta con ningún ensayo clínico ni publicación, y el fenotipo predicho (susceptibilidad) no es una condición tratable. Por eso queda en nivel L5 y no hay base para avanzar.

**Para avanzar se necesita:**
- Definir si existe una condición clínica tratable detrás de este fenotipo, o descartar la predicción.
- Obtener los datos de mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de INVIMA (advertencias y contraindicaciones), que sigue pendiente y bloquea el tamizaje de seguridad.
- Conciliar la indicación original con el texto aprobado, porque el registro solo dice «ENZALUTAMIDA».
- Como referencia, la predicción «cáncer de órgano reproductor masculino» (puesto 6) tiene evidencia de nivel L1 con ensayos de fase 3 y fase 2. Sin embargo, es un uso ya concordante con la indicación aprobada y no un reposicionamiento nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

