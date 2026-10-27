---
layout: default
title: Cefalotin
parent: Solo Predicción del Modelo (L5)
nav_order: 141
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Cefalotin: nueva indicación predicha, Uretritis gonocócica (nivel de evidencia L5). Indicación original: CEFALOTINA"
monitor_inn: "cefalotin"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "bronchitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "congenital analbuminemia"]
---

# Cefalotin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Cefalotina: De Uso Antibacteriano Registrado a Uretritis Gonocócica
{: .text-alpha }

## Resumen en Una Frase

Cefalotina es una cefalosporina de primera generación, registrada en Colombia como antibiótico inyectable (el texto de indicación registrado solo indica el nombre del principio activo).
El modelo TxGNN predice que podría ser efectiva para **uretritis gonocócica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | CEFALOTINA (el registro sanitario no detalla una indicación específica) |
| Nueva Indicación Predicha | Uretritis gonocócica |
| Puntaje de Predicción TxGNN | 99.25% |
| Nivel de Evidencia | L4 (según la evaluación de la predicción; sin estudios clínicos ni literatura aportados) |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 3 (0 vigentes, 3 cancelados) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Cefalotina es una cefalosporina de primera generación que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas fijadoras de penicilina. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada, pero esta descripción corresponde a la clase farmacológica conocida. Tiene buena actividad frente a bacterias Gram-positivas y actividad variable frente a Gram-negativas.

Neisseria gonorrhoeae es, en términos de clase, un blanco antibacteriano plausible. Sin embargo, las cefalosporinas de primera generación tienen actividad limitada contra este microorganismo, y las guías actuales prefieren cefalosporinas de tercera generación como ceftriaxona. El puntaje alto de TxGNN probablemente refleja asociaciones a nivel de clase antibacteriana y no evidencia específica del fármaco.

Además, el producto no está comercializado actualmente en Colombia y es de administración exclusivamente parenteral. La plausibilidad mecanística es, por tanto, solo indirecta.

### Otras predicciones del modelo

| Posición | Enfermedad predicha | Puntaje | Nivel | Valoración |
|------|------|------|------|------|
| 2 | Uretritis por Ureaplasma | 99.25% | L5 | Contradicha mecanísticamente: Ureaplasma carece de pared celular, por lo que los betalactámicos no deberían ser eficaces |
| 3 | Bronquitis | 99.25% | L4 | Plausibilidad indirecta; la mayoría de las bronquitis agudas son virales y no requieren antibióticos |
| 4 | Síndrome de hiperviscosidad policlonal | 99.16% | L5 | Sin mecanismo plausible; probable artefacto del grafo de conocimiento |
| 5 | Hiperamilasemia | 99.16% | L5 | Es un hallazgo de laboratorio, sin fundamento antibacteriano; probable artefacto |
| 6 | Enfermedad inflamatoria uterina | 99.11% | L4 | Plausibilidad indirecta; hoy se prefieren regímenes con cefoxitina o cefotetán |
| 7 | Pielonefritis xantogranulomatosa | 99.09% | L4 | Plausibilidad indirecta; el manejo es principalmente quirúrgico |
| 8 | Analbuminemia congénita | 99.01% | L5 | Trastorno genético sin base infecciosa; probable artefacto |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

Los tres registros sanitarios están cancelados; actualmente no hay productos vigentes.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20170303 | CEFALOTINA SÓDICA 1G/VIAL | Polvo estéril para reconstituir a solución inyectable | CEFALOTINA | Cancelado |
| 20192711 | CEFALODELT® | Polvo para solución inyectable | CEFALOTINA | Cancelado |
| 20200906 | CEFALOTINA 1G POLVO PARA RECONSTITUIR A SOLUCIÓN INYECTABLE | Polvo estéril para reconstituir a solución inyectable | CEFALOTINA | Cancelado |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 14 interacciones. Las 12 de nivel moderado son con:
  - Aminoglucósidos: kanamicina, neomicina, estreptomicina, amikacina (incluida la forma liposomal) y gentamicina
  - Otros fármacos: ácido picosulfúrico, warfarina, cloranfenicol, etinilestradiol, ácido micofenólico y pemetrexed
- **Transportadores**: cefalotina inhibe el transportador de aniones orgánicos OAT3 (SLC22A8) y también se asocia con OAT4 (SLC22A11). Esto podría alterar la eliminación renal de otros fármacos que usen estas vías.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que respalden ninguna de las indicaciones predichas. Además, las cefalosporinas de primera generación no son de elección para uretritis gonocócica, varias predicciones están mecanísticamente contradichas o parecen artefactos del grafo, y el producto no tiene registros vigentes en Colombia.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de INVIMA para advertencias y contraindicaciones
- Completar los datos del mecanismo de acción desde DrugBank
- Revisar la literatura sobre sensibilidad de *N. gonorrhoeae* a cefalotina frente a alternativas actuales como ceftriaxona
- Evaluar si tiene sentido reposicionar un fármaco sin registro vigente frente a antibióticos disponibles y mejor respaldados
- Evaluar la compatibilidad de vías de administración (solo parenteral)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

